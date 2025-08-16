import pandas as pd

class convertDatasets:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def load_df(self, cols) -> pd.DataFrame:
        df = pd.read_csv(self.file_path, header=None, names=cols)
        for c in cols:
            df[c] = df[c].astype("category")
        return df

    def stats(self, df: pd.DataFrame,  strict: bool = False) -> pd.DataFrame:
        before_na = df.isna().sum()
        num = df.apply(pd.to_numeric, errors="coerce")
        after_na = num.isna().sum()
        newly_na = (after_na - before_na)
        bad = newly_na[newly_na> 0]
        if not bad.empty:
            msg = "unconvertible values appeared in below cols, were set to 'NaN:' \n" + bad.to_string()
            if strict:
                raise ValueError(msg)
            else:
                print("warn!", msg)


        base = num.agg(["max", "min", "mean"]).T
        abs_stats = num.abs().agg(["max", "min", "mean"]).T.add_prefix("absolute_")
        out = base.join(abs_stats)
        out = out.drop(index="class", errors="ignore")

        print(out.to_string(float_format=lambda x: f"{x:.2f}" if pd.notna(x) else "NaN"))
        return out

def main():
    cols = ["sepal length", "sepal width", "petal length", "petal width", "class"]
    cd = convertDatasets("iris.data")
    df_parquet = cd.load_df(cols)
    cd.stats(df_parquet)
    return 0

if __name__ == "__main__":
    main()
    