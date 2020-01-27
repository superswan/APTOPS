import pandas as pd
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

pd.set_option('display.max_colwidth',100)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/tables")
def show_tables():
    xls = pd.ExcelFile('apt.xlsx')
    sheets = []
    titles = [""]
    tables = []
    countrycodes = ["","CN", "RU", "KP", "IR", "IL", "US", "ME", "OT", "RD"]
    for idx,name in enumerate(xls.sheet_names[1:10]):
        titles.append(name)
        sheets.append(pd.read_excel(xls, sheet_name = name, header=1))

    for idx,sheet in enumerate(sheets):
        tables.append(sheets[idx].to_html(classes="table table-dark table-striped table-bordered table-hover table-sm table-data",
        index=False, na_rep="N/A", render_links=True, justify="center", col_space=500))

    return render_template('view.html', tables=tables, titles=titles, countrycode=countrycodes)

if __name__ == '__main__':
    app.run(debug=True)

