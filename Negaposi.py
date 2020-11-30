import os
import glob
import pymysql
from flask import Flask,render_template,request,redirect,session,url_for

app=Flask(__name__)
app.secret_key="secret"

#ログインに使うユーザ名とパスワード
USERLIST={
    "taro":"aaa",
    "jiro":"bbb",
    "sabu":"ccc",
    "nagaokun":"hokuryu",
}

#パンくずリスト用
pankuzu_list=list()


#ログインチェック処理
def try_login(user, password):
    #ユーザがリストにあるか?
    if not user in USERLIST:
        return False
    #パスワードが合ってるか?
    if USERLIST[user] != password:
        return False
    #ログイン処理を実行
    session["login"]=user
    return True

#Mysqlオプション
MYSQL_OPTIONS={
    "host":"127.0.0.1",
    "port":3307,
    "user":"root",
    "passwd":"admin",
    "db":"lab_impressions_mysql"
}

#データベースコネクション獲得
def getConnection():
    conn=pymysql.connect(
        host=MYSQL_OPTIONS["host"],
        port=MYSQL_OPTIONS["port"],
        user=MYSQL_OPTIONS["user"],
        passwd=MYSQL_OPTIONS["passwd"],
        db=MYSQL_OPTIONS["db"],
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

#lab_valとyear_valの値によって取得するデータベースを分ける
def get_lab_impressions(lab_val,year_val):
    conn=getConnection()
    if lab_val==1 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=1 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==1 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=1 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==2 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=2 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==2 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=2 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==3 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=3 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==3 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=3 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==4 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=4 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()

    elif lab_val==4 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=4 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()

    elif lab_val==5 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=5 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==5 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=5 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==6 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=6 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==6 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=6 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==7 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=7 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==7 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=7 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==8 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=8 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==8 and year_val==2020:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=8 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    elif lab_val==9 and year_val==2019:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=9 and year=2019;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    else:
        try:
            with conn.cursor() as cursor:
                sql="SELECT lab_name, impressions FROM lab_impressions WHERE lab_num=9 and year=2020;"
                cursor.execute(sql)
                result=cursor.fetchall()
        finally:
            conn.close()
    result_list=list()
    for row in result:
        result_list.append({"lab_name":row["lab_name"],"impressions":row["impressions"]})
    return result_list

@app.route("/")
def index():
    #ログインフォーム
    return render_template("login_form.html")

@app.route("/login", methods=["GET","POST"])
def login():
    # try:
    #     with conn.cursor() as cursor:
    #         sql="SELECT user_name, password FROM user_login"
    #フォームの値を取得
    user=None
    password=None
    if "UserName" in request.form:
        user=request.form["UserName"]
    if "PassWord" in request.form:
        password=request.form["PassWord"]
    if (user is None) or (password is None):
        return redirect("login_form.html", error_message="ユーザ名またはパスワードが間違っています!再入力してください!")
    #ログインチェック
    if try_login(user, password) == False:
        return render_template("login_form.html", error_message="ユーザ名、パスワードを入力してください!")
        #return redirect("/")
    return redirect(url_for("login2"))

@app.route("/login2")
def login2():
    if "login" not in session:
        return redirect("/")
    pankuzu_list=list()
    pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
    return render_template("select_lab.html",pankuzu_list=pankuzu_list)

#研究室一覧の画面に遷移
@app.route("/select_lab", methods=["GET","POST"])
def select_lab():
    name=None
    if request.method == "POST":
        if request.form.get("lab-options") and request.form.get("select-lab-submit"):
            #研究室の選択結果をsessionに追加
            session["lab-options"]=request.form.get("lab-options")
            return redirect(url_for("select_lab2"))

#フォームの再送信を防止(PRGパターン)    
@app.route("/select_lab2")
def select_lab2():
    #研究室を分けるためのグローバル変数
    global lab_val
    if "lab-options" not in session:
        return redirect(url_for("select_lab"))
    LabOptions=session["lab-options"]
    options="{}".format(LabOptions)
    #吉田研究室1
    if "吉田研究室1" in options:
        lab_val=1
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #吉田研究室2
    elif "吉田研究室2" in options:
        lab_val=2
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #古家研究室
    elif "古家研究室" in options:
        lab_val=3
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #行天研究室
    elif "行天研究室" in options:
        lab_val=4
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #高見研究室
    elif "高見研究室" in options:
        lab_val=5
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #紙名研究室
    elif "紙名研究室" in options:
        lab_val=6
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #西野研究室
    elif "西野研究室" in options:
        lab_val=7
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #大竹研究室
    elif "大竹研究室" in options:
        lab_val=8
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)
    #中島研究室
    else:
        lab_val=9
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        return render_template("select_year.html", pankuzu_list=pankuzu_list, options=options)

#年度一覧の画面に遷移
@app.route("/select_year", methods=["GET", "POST"])
def select_year():
    #年度を分けるためのグローバル変数
    global year_val
    if request.method == "POST":
        if request.form.get("year-options") and request.form.get("select-year-submit"):
            #年度の選択結果をsessionに追加
            session["year-options"]=request.form.get("year-options")
            YearOptions=session["year-options"]
            session["select-year-submit"]=request.form.get("select-year-submit")
            year_options="{}".format(YearOptions)
            if "2019年" in year_options:
                year_val=2019
                return redirect(url_for("select_year2"))
            else:
                year_val=2020
                return redirect(url_for("select_year2"))

#フォームの再送信を防止(PRGパターン)
@app.route("/select_year2")
def select_year2():
    if "year-options" and "select-year-submit" in session:
        impressions_list=get_lab_impressions(lab_val,year_val)
        pankuzu_list=list()
        pankuzu_list.append({"href":"/logout","display_name":"ログアウト"})
        pankuzu_list.append({"href":"/login2","display_name":"研究室一覧"})
        pankuzu_list.append({"href":"/select_lab2","display_name":"年一覧"})
        return render_template("lab_impressions.html",pankuzu_list=pankuzu_list,impressions_list=impressions_list)
    
@app.route("/logout")
def logout():
    session.pop("login", None)
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)