# Dalsi priklad API, ktery ze sluzby Polygon.IO stahuje akciova data. Verze zdarma je omezena na 5 pozadavku minuta. Podminkou je mit .csv soubor s jednotlivymi nazvy tickeru pod headerem Symbol.
# V tomto ale stahujete predpripavenou Pythoni knihovnu (coz je casto standardem pro lepsi services).

import argparse
import pandas as pd
from polygon import RESTClient
from time import sleep
from pathlib import Path
def record(args):
    key = args.key
    tickers = pd.read_csv(args.tickers)['Symbol'].to_list()
    if args.end == '':
        to = pd.to_datetime(pd.Timestamp.today())
    else:
        to = pd.to_datetime(args.end)
    if args.start == '':
        from_ = to - pd.Timedelta('730d')
    else:
        from_ = pd.to_datetime(args.start)
    for ticker in tickers:
        print(f"Working on {ticker}")
        daterange = pd.date_range(from_, to, freq='3M').strftime('%Y-%m-%d')
        daterange = daterange.append(pd.Index([to.strftime('%Y-%m-%d')]))
        ticker_path = Path(ticker).resolve()
        ticker_path.mkdir(exist_ok=True)
        list_for_df = []
        for i in range(1, len(daterange)):
            start = daterange[i - 1]
            end = daterange[i]
            temp_file = Path(ticker_path / f'{ticker}_1m_ohlcv_{start}_{end}.pkl')
            if temp_file.is_file():
                print(f'Skipping: {ticker}_1m_ohlcv_{start}_{end}.pkl')
                continue
            with RESTClient(key) as client:
                if args.free:
                    sleep(15) # Sleep 15 seconds to submit ~5 requests per second for free Polygon account
                resp = client.stocks_equities_aggregates(ticker, 1, "minute", start, end, unadjusted=False, limit=50000)
                try:
                    list_for_df.extend(resp.results)
                    df_temp = pd.DataFrame(resp.results)
                except AttributeError:
                    print(f'Can\'t process: {ticker}_1m_ohlcv_{start}_{end}.pkl')
                    continue
                assert len(df_temp) <= 50000
                print(f'Saving: {ticker}_1m_ohlcv_{start}_{end}.pkl')
                df_temp.to_pickle(temp_file)
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Polygon IO 1min OHLCV recorder')
    parser.add_argument('--end', default='', type=str)
    parser.add_argument('--start', default='', type=str)
    parser.add_argument('--key', type=str)
    parser.add_argument('--tickers', type=str)
    parser.add_argument('--free', action='store_true')
    args = parser.parse_args()
    record(args)