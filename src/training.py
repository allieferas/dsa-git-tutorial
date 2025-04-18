from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from pathlib import Path
import joblib


tree = pd.read_csv('data/processed/clean_trees.csv')

train, test = train_test_split(tree, train_size=0.8, test_size=0.2, random_state=42)

target='Property Benefits ($)'
xcols = [c for c in train.columns if c != target]
# a comment
lr = LinearRegression()
lr.fit(train[xcols],train[target])
test['prediction'] = lr.predict(test[xcols])

#beep boop

outdir = Path('data/out')
outdir.parent.mkdir(exist_ok=True, parents=True)
test.to_csv(outdir.joinpath('predictions.csv'),index=False)

joblib.dump(lr, outdir.joinpath('model.joblib'))


