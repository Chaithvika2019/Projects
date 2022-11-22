from flask import Flask,render_template,request
from bs4 import BeautifulSoup as but
#here 1,2,4,5,lines are modules..
from urllib.request import urlopen as uropen
import requests



app=Flask(__name__)
@app.route("/",methods=["GET"])
def tag_1():
    return render_template("TV.html")


@app.route('/review',methods=["GET","POST"])
def new_line():
    if request.method=="POST":
        try:
            searchString=request.form['content'].replace(" ","")
            print(searchString)
            Tv_Url="https://www.flipkart.com/search?q="+searchString
            scrap_amezon = uropen(Tv_Url)
            scrap_detail = scrap_amezon.read()
            scrap_amezon.close()
            scrap_buti = but(scrap_detail, "html.parser")
            # print(scrap_buti)
            scrap_2 = scrap_buti.find_all("div", {"class": "_1AtVbE col-12-12"})
            del scrap_2[0:2]
            tv_product_link= "https://www.flipkart.com" +scrap_2[0].div.div.div.a["href"]
            #this line is for web page link
            all_1=but(tv_product_link, "html.parser")
            All_2 = requests.get(all_1)
            All_2.encoding="utf-8"
            All_tv = but(All_2.text, "html.parser")
            Tv_review = All_tv. find_all("div", {"class": "_16PBlm"})
            TV_info = []
            #this line is creat empty list
            for Tv in Tv_review:
                # this line is for_loop

                try:
                    TvName = All_tv.find_all("span", class_="B_NuCI")[0].text
                #this line for Tv name
                except:
                    TvName = "TvName is not available here"
                try:
                    TvRating = Tv.find_all("div", class_="_3LWZlK")[0].text
                #this line for Tv rating
                except:
                    TvRating = "TvRating is not available here"
                try:
                    TvPrice =All_tv.find_all("div", class_="_30jeq3 _16Jk6d")[0].text
                         # this line for Tv price
                except:
                    TvPrice = "TvPrice is not available here"
                try:
                    TvRewever_name = Tv.find_all("p", class_="_2sc7ZR _2V5EHH")[0].text
                             # this line for Tv Revever name
                except:
                    TvRewever_name = "TvRewever_name  is not avialable here"
                try:
                    TvHead_Comment = Tv.find_all("p", class_="_2-N8zT")[0].text

                #this line for Tv head comment

                except:
                    TvHead_Comment = "TvHead_Comment is not available here"
                try:
                    TvMain_Comment = Tv.find_all("div", class_="")[0].text
                # this try block will execute Tv main comment

                except:
                    TvMain_Comment = "TvMain_Comment is not available here"

                Tv_in={"TvName":searchString,"TvRating":TvRating,"TvPrice":TvPrice,"TvRewever_name":TvRewever_name,
                       "TvHead_Comment ":TvHead_Comment ,"TvMain_Comment":TvMain_Comment}
                #these lines are created dictionary 63,64 lines

                TV_info.append(Tv_in)
                                       # this line for appending the dictionary
                print(TV_info)
            return render_template("Results.html", reviews=TV_info[0:len(TV_info)-1])

        except:
            return"UMA"











app.run()