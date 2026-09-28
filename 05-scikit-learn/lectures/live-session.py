# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas",
#     "plotnine",
#     "altair",
#     "palmerpenguins",
#     "scikit-learn",
# ]
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python versus R
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Pandas
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```R
    library("tidymodels")

    linear_reg()
    ```
    """)
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _():
    # from pandas import read_csv
    return


@app.cell
def _():
    # pd.read_csv()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Plotnine

    https://plotnine.readthedocs.io/en/latest/

    In Jupyter you can write `from plotnine import *`. Marimo does not allow
    star imports, so here we write `import plotnine as p9` and use `p9.ggplot`,
    `p9.aes`, and so on.
    """)
    return


@app.cell
def _():
    import plotnine as p9
    from plotnine.data import mtcars

    return mtcars, p9


@app.cell
def _(mtcars):
    mtcars
    return


@app.cell
def _(mtcars, p9):
    (
        p9.ggplot(mtcars, p9.aes(x = "wt", y = "mpg", color = "factor(gear)"))
         + p9.geom_point()
         + p9.stat_smooth(method="lm")
         + p9.facet_wrap("~gear")
         + p9.theme(figure_size = (4, 3))
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Altair

    https://altair-viz.github.io/
    """)
    return


@app.cell
def _():
    from palmerpenguins import load_penguins

    return (load_penguins,)


@app.cell
def _():
    import altair as alt

    return (alt,)


@app.cell
def _(load_penguins):
    penguins = load_penguins()

    penguins.head()
    return (penguins,)


@app.cell
def _(alt, penguins):
    # pipe-ing uses dots instead of |>

    alt.Chart(penguins).mark_point().encode(
        x = alt.X('bill_depth_mm', scale=alt.Scale(zero=False)),
        y = alt.Y('bill_length_mm', scale=alt.Scale(zero=False)),
        color = alt.Color('species'),
        tooltip = [alt.Tooltip('species'), alt.Tooltip('sex')]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Scikit-Learn
    """)
    return


@app.cell
def _(penguins):
    penguins2 = (
        penguins
        .dropna()
        .pipe(lambda df_: df_[df_['species']=="Adelie"])
    )

    penguins2.head()
    return (penguins2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```R
    mod = linear_reg() |> set_engine("lm")

    mod_fit = mod |> fit(bill_length_mm ~ bill_depth_mm, data = penguins)
    ```
    """)
    return


@app.cell
def _():
    list_of_stuff = [1, 2, 5, 6]
    list_of_stuff
    return


@app.cell
def _():
    features = ['bill_depth_mm']
    features
    return (features,)


@app.cell
def _():
    outcome = ['bill_length_mm']
    return


@app.cell
def _(features, penguins2):
    # in R: X = penguins2 |> select(bill_depth_mm)

    X = penguins2[features] # capitalized
    y = penguins2[['bill_length_mm']]

    X.head()
    return X, y


@app.cell
def _():
    from sklearn.linear_model import LinearRegression

    return (LinearRegression,)


@app.cell
def _(LinearRegression, X, y):
    mod = LinearRegression()

    mod.fit(X, y)

    mod
    return (mod,)


@app.cell
def _(mod):
    # in R: tidy(mod_fit)

    mod.intercept_
    return


@app.cell
def _(pd):
    X_to_predict = pd.DataFrame(
        {"bill_depth_mm": [19]}
    )

    X_to_predict
    return (X_to_predict,)


@app.cell
def _(X_to_predict, mod):
    # augment, predict
    # in R: mod |> predict(new_data = penguins)

    mod.predict(X_to_predict)
    return


@app.cell
def _(p9, penguins2):
    p = (
        p9.ggplot(penguins2, p9.aes(x = "bill_depth_mm", y = "bill_length_mm")) + 
        p9.geom_point() +
        p9.theme(figure_size = (4, 3))
    )

    p
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Transforming input data
    """)
    return


@app.cell
def _():
    from sklearn.compose import make_column_transformer
    from sklearn.preprocessing import OneHotEncoder

    return OneHotEncoder, make_column_transformer


@app.cell
def _():
    features2 = ['bill_depth_mm', 'species']
    features2
    return (features2,)


@app.cell
def _(features2, penguins):
    penguins_no_missing = penguins.dropna()

    X2 = penguins_no_missing[features2] # capitalized
    y2 = penguins_no_missing[['bill_length_mm']]

    X2.head()
    return X2, y2


@app.cell
def _(OneHotEncoder, make_column_transformer):
    ct = make_column_transformer(
        ['passthrough', ['bill_depth_mm']],
        [OneHotEncoder(drop=['Adelie']), ['species']]
    )
    return (ct,)


@app.cell
def _(ct):
    ct
    return


@app.cell
def _(X2, ct):
    ct.fit_transform(X2)[:5]

    # try fit then transform
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Pipelines
    """)
    return


@app.cell
def _():
    from sklearn.pipeline import make_pipeline

    return (make_pipeline,)


@app.cell
def _(LinearRegression, X2, ct, make_pipeline, y2):
    # marimo runs cells in order of what they use, so fit in the same cell
    pl = make_pipeline(
        ct,
        LinearRegression()
    )

    pl.fit(X2, y2)
    return (pl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Extract steps from pipeline
    """)
    return


@app.cell
def _(pl):
    list(pl.named_steps.keys())
    return


@app.cell
def _(pl):
    pl.named_steps['linearregression']
    return


@app.cell
def _(pl):
    mod_from_pipeline = pl['linearregression']
    mod_from_pipeline.intercept_
    return


@app.cell
def _(pd):
    X_to_predict2 = pd.DataFrame(
        {"bill_depth_mm": [19],
         "species": ["Adelie"]}
    )
    return (X_to_predict2,)


@app.cell
def _(X_to_predict2, pl):
    pl.predict(X_to_predict2)
    return


if __name__ == "__main__":
    app.run()
