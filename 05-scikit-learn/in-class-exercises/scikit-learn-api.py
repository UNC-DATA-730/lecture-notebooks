# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas",
#     "plotnine",
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
    mo.callout('Each variable can be defined in only one cell. If you get a "multiple definitions" error, give the variable a new name. Cells re-run on their own when the cells they use change.', kind='info', title='Tip')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        "Some cells below will show errors when you first open this notebook. That is expected! They use variables from the blank cells you fill in. Once you complete a blank cell, the cells below it re-run on their own and the errors go away.",
        kind="warn",
        title="Heads up: errors are normal at first",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Run the following cell to import all the code we need to complete the exercise.

    In Jupyter you can write `from plotnine import *`. Marimo does not allow
    star imports, so here we write `import plotnine as p9` and use `p9.ggplot`,
    `p9.aes`, `p9.geom_point`, and so on.
    """)
    return


@app.cell
def _():
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import make_column_transformer
    from sklearn.pipeline import make_pipeline

    import plotnine as p9

    import pandas as pd

    return (
        LinearRegression,
        LogisticRegression,
        OneHotEncoder,
        make_column_transformer,
        make_pipeline,
        pd,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will use a subset of the [General Social Survey](https://gss.norc.org/) (GSS), a long-running survey of U.S. adults. This is the same data used in [Chapter 10 of *Elements of Data Science*](https://allendowney.github.io/ElementsOfDataScience/10_regression.html).

    The columns we will use:

    - `realinc`: household income, in constant dollars
    - `educ`: years of education
    - `sex`: `male` or `female`
    - `age`: age in years
    - `grass`: "Do you think the use of marijuana should be made legal or not?" (`1` = legal, `2` = not legal)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use `pd.read_csv` to read in this data and call the new dataframe `df_gss`. We keep only the 2024 survey and give `sex` readable labels.

    Use the snippet below 👇.
    ```python
    df_gss = (
        pd.read_csv('https://raw.githubusercontent.com/UNC-BIOS-512/jupyterlite/refs/heads/main/data/gss_subset.csv')
        .query('year == 2024')                                               # keep one survey year
        .assign(sex=lambda df_: df_['sex'].map({1: 'male', 2: 'female'}))   # 1/2 -> male/female
    )

    df_gss.head()                                                            # preview the table
    ```
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's build a model of `realinc` using the `educ` and `sex` variables.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First we'll make a preprocessor to dummy encode the `sex` column and pass the `educ` through untransformed to our model.

    /// details | Hint
    ```python
    ct = make_column_transformer(
        ['passthrough', ['educ']],
        [OneHotEncoder(drop=['female']), ['sex']]
    )
    ```
    ///
    """)
    return


@app.cell
def _(OneHotEncoder, make_column_transformer):
    # fix the following code and execute the cell

    ct = make_column_transformer(
        ['passthrough', ['FILL_IN_THE_PASSTHROUGH_COLUMN(S)_HERE']],
        [OneHotEncoder(drop=['female']), ['FILL_IN_THE_COLUMN_TO_ENCODE_HERE']]
    )
    return (ct,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's create our training data. We drop rows with missing values in our model columns, establish our `outcome` variable, and will send the rest of the data to our modeling pipeline.
    """)
    return


@app.cell
def _(df_gss):
    df_lm = df_gss.dropna(subset=['realinc', 'educ', 'sex'])

    outcome = 'realinc'

    # idiomatically "X" stands for training data and "y" for the outcome
    X, y = df_lm.loc[:, df_lm.columns != outcome], df_lm[outcome]
    return X, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Preview the training data `X` to confirm our outcome is no longer in the training data.

    /// details | Hint
    ```python
    X.head()
    ```
    ///
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use the `fit_transform` method for your column transformer to see how it transforms your training data. I.e. call `fit_transform` with `X` as the argument.

    /// details | Hint
    ```python
    ct.fit_transform(X)[:5]   # first 5 rows
    ```
    ///
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we'll build out pipeline/model. Execute the following cell. Does the output make sense? Can you find which columns were passed through your column transformer by clicking through the output pipeline visualization?
    """)
    return


@app.cell
def _(LinearRegression, X, ct, make_pipeline, y):
    pl = make_pipeline(
        ct, # or whatever you called your column transformer
        LinearRegression()
    )

    pl.fit(X, y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Make a new dataframe called `df_lm_w_pred` by calling the following method from the `df_lm` dataframe: `.assign(pred_realinc=lambda df_: pl.predict(df_))`.

    What is the name of your predictions column?

    /// details | Hint
    ```python
    df_lm_w_pred = df_lm.assign(pred_realinc=lambda df_: pl.predict(df_))

    df_lm_w_pred.head()
    ```

    The predictions column is `pred_realinc`.
    ///
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use Plotnine and your `df_lm_w_pred` dataframe to plot your model. Put `educ` on the x-axis and color by `sex`. Use `p9.geom_point` for your observed values (`realinc`) and `p9.geom_line` for your predicted values (`pred_realinc`).

    /// details | Hint
    ```python
    (
        p9.ggplot(df_lm_w_pred, p9.aes(x='educ', y='realinc', color='sex'))
        + p9.geom_point(alpha=0.3)
        + p9.geom_line(p9.aes(y='pred_realinc'), size=1)
        + p9.theme(figure_size=(4, 3))   # width, height in inches
    )
    ```
    ///
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use the function below to show the regression table for your model.

    /// details | Hint
    ```python
    get_regression_table(pl)
    ```
    ///
    """)
    return


@app.cell
def _(pd):
    def get_regression_table(pipeline):

        ct = pipeline['columntransformer']
        terms = list(ct.get_feature_names_out()) + ['intercept']

        mod = pipeline['linearregression']
        coefs = mod.coef_
        intercept = mod.intercept_
        estimates = list(coefs) + [intercept]

        data = {
            "term": terms,
            "estimate": estimates
        }

        return pd.DataFrame(data)

    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    😎 **BONUS** inspect the function above. How do you access the "model" from a pipeline? What about the coefficients for your model terms?

    /// details | Hint
    Get a step from a pipeline by its name, like a dictionary: `pipeline['linearregression']`. The coefficients are in the model's `.coef_` attribute, and the intercept is in `.intercept_`.

    ```python
    pl['linearregression'].coef_
    ```
    ///
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Average marginal effects with AI

    Now let's model a yes/no outcome: does the person think marijuana should be legal? We use logistic regression with `age` and `educ`.

    A logistic model predicts a *probability*, and it is not a straight line. So the coefficients are not "change in probability per year". The **average marginal effect** (AME) answers that question: on average, how much does the probability change for one more year of age (or education)?

    Run the cell below to fit the model.
    """)
    return


@app.cell
def _(LogisticRegression, df_gss):
    df_grass = (
        df_gss.dropna(subset=['grass', 'age', 'educ'])
        .assign(legal=lambda df_: (df_['grass'] == 1).astype(int))   # 1 = legal, 0 = not legal
    )

    X_logit = df_grass[['age', 'educ']]
    y_logit = df_grass['legal']

    m = LogisticRegression().fit(X_logit, y_logit)
    m
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instead of writing the AME code yourself, use marimo's built-in AI. Add a new cell below, choose **Generate with AI**, and paste this prompt:

    > I have a fitted scikit-learn `LogisticRegression` called `m`, trained on `X_logit` (columns `age` and `educ`). Write code that computes the average marginal effect of each predictor with the analytic formula: coefficient × mean of p·(1−p), where p is the predicted probability of class 1. Show the result as a small pandas DataFrame with columns `term` and `ame`.
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Check the AI's work and answer these questions:

    1. Does the code use `m.predict_proba(X_logit)[:, 1]` to get the probability of class 1? Why `[:, 1]`?
    2. Does the code match the formula in the prompt?
    3. What does the AME for `age` mean in words? What about `educ`?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Show one answer": mo.md(r"""
    ```python
    p = m.predict_proba(X_logit)[:, 1]
    ame_analytic = m.coef_[0] * (p * (1 - p)).mean()
    ```
    """)
        }
    )
    return


if __name__ == "__main__":
    app.run()
