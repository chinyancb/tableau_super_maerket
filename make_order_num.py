import sys
import pandas as pd


def main():
    
    FILENAME = 'サンプル - スーパーストア.xls'

    # エクセルファイル読み込み
    df = pd.read_excel(f'./{FILENAME}')
    
    # 行数を取得
    df_row_tmp = df.shape[0]

    # 全体の購入順、カテゴリ購入順、サブカテゴリ購入順、製品購入順を作成
    df['購入順'] = df.groupby('顧客 ID')['オーダー日'].rank(ascending=True, method='min')
    df['カテゴリ購入順'] = df.groupby(['顧客 ID', 'カテゴリ'])['オーダー日'].rank(ascending=True, method='min')
    df['サブカテゴリ購入順'] = df.groupby(['顧客 ID', 'サブカテゴリ'])['オーダー日'].rank(ascending=True, method='min')
    df['製品購入順'] = df.groupby(['顧客 ID', '製品 ID'])['オーダー日'].rank(ascending=True, method='min')


    # データフレームの行数が変わっていないか確認
    if df.shape[0] != df_row_tmp:
        print(f'rows changed. row:{df.shape[0]}, original row:{df_row_tmp}')
        sys.exit(1)

    # csvとして出力
    df.to_csv(f'./{FILENAME}_購入順.csv', header=True, index=False)




if __name__ == '__main__':
   main() 
