from flask import jsonify,Flask,render_template,redirect,request
from waitress import serve
from db import login,signin

app = Flask("__name__")


@app.route('/')
def home():
#     link image of logo to this url ---- <a href="{{ url_for('home') }}"> in 'index.html'
      return render_template("home.html")
  
@app.route('/about')
def about():
    return render_template("about.html")



##inside academics
    ##department
@app.route('/academics/department/CSE/Btech')
def department_CSE_Btech(): #
    return render_template("about_cse_Btech.html")
@app.route('/academics/department/CSE/Mtech')
def department_CSE_mtech(): #
    return render_template("about_cse_mtech.html")

@app.route('/academics/department/CSE-AIML')
def department_CSE_AIML(): 
    return render_template("about__Btech_CSE-AIML.html")
@app.route('/academics/department/CSE_Cyber')
def department_CSE_Cyber(): #
    return render_template("about_cse_cyber.html")
@app.route('/academics/department/Civil_engg')
def department_Civil_engg(): #
    return render_template("about_Civil_engg.html")
@app.route('/academics/department/ECE')
def department_ECE(): #
    return render_template("about_ECE.html")

    ##campus life
@app.route('/academics/campus_life/Hostel')
def campus_life_Hostel():
    return render_template("campus_life_Hostel.html")
@app.route('/academics/campus_life/library')
def campus_life_library():
    return render_template("campus_life_library.html")


    ## academics
@app.route('/academics/admission_process')
def admission_process():
    return render_template("admission_process.html")
@app.route('/academics/admission_inquiry')
def admission_inquiry():
    return render_template("admission_inquiry.html")
@app.route('/academics/admission_Feerefund')
def admission_Feerefund():
    return render_template("admission_Feerefund.html")
@app.route('/academics/admission_feeStructure')
def admission_feeStructure():
    return render_template("admission_feeStructure.html")


    ##student techer login
@app.route('/academics/Student_login')
def Student_login():
    return redirect('https://portal.lnct.ac.in/Accsoft2/studentlogin.aspx')
@app.route('/academics/Employ_login')
def Employ_login():
    return redirect('https://portal.lnct.ac.in/Accsoft2/login.aspx')


# @app.route('/news-events')
# def news_events():
#     return render_template("news.html")


@app.route('/alumni')
def alumni_page():
    return render_template("alumni.html")
@app.route('/alumni/talk')
def talk():
    return render_template("alumni_talk.html")
@app.route('/alumni/photos')
def photos():
    return render_template("alumni_photos.html")


# @app.route('/placement')
@app.route('/placement/records')
def placement_records():
    # Example: fetch placed students from DB
    placed_students = [
        {"name": "Alice", "company": "Google"},
        {"name": "Bob", "company": "Microsoft"},
    ]
    return render_template('placement_records.html', students=placed_students)

# 2) Placement Brochure (serve a PDF file)
@app.route('/placement/brochure')
def placement_brochure():
    brochure_path = 'static/files/placement_brochure.pdf'
    return send_file(brochure_path, as_attachment=True)

# 3) Training Info
@app.route('/placement/training')
def placement_training():
    # Example training info
    training_data = {
        "courses": ["Resume Building", "Interview Preparation", "Technical Skills"],
        "schedule": "Every Monday and Wednesday, 5-7 PM"
    }
    return render_template('placement_training.html', training=training_data)

# 4) Company/Recruiters Info
@app.route('/placement/company')
def placement_company():
    companies = ["Google", "Microsoft", "Amazon", "Facebook"]
    return render_template('placement_company.html', companies=companies)



# @app.route('/colleges')
# -------------------- 🔵 College Routes --------------------

@app.route('/colleges/lnctvu')
def lnctvu():
    return redirect("https://lnctvu.ac.in")

@app.route('/colleges/jnctpu')
def jnctpu():
    return redirect("https://jnctpu.edu.in")

@app.route('/colleges/indorelnmc')
def indorelnmc():
    return redirect("https://indorelnmc.in")

@app.route('/colleges/jncn')
def jncn():
    return redirect("https://jncn.ac.in")

@app.route('/colleges/cecibalsapur')
def cecibalsapur():
    return redirect("https://cecibalsapur.ac.in")

@app.route('/colleges/lncps')
def lncps():
    return redirect("https://lncps.in")

@app.route('/colleges/lnctuj')
def lnctuj():
    return redirect("https://lnctuj.com")

@app.route('/colleges/lncts')
def lncts():
    return redirect("https://lncts.in")

@app.route('/colleges/lnctmca')
def lnctmca():
    return redirect("https://lnctmca.in")

@app.route('/colleges/lncpbhopal')
def lncpbhopal():
    return redirect("https://lncpbhopal.in")

@app.route('/colleges/lnctbhopal')
def lnctbhopal():
    return redirect("https://lnctbhopal.in")

@app.route('/colleges/lncte')
def lncte():
    return redirect("https://lncte.in")

@app.route('/colleges/lnctbblindorecampus')
def lnctbblindorecampus():
    return redirect("https://lnctbblindorecampus.in")

@app.route('/colleges/lnctrishiraj')
def lnctrishiraj():
    return redirect("https://lnctrishiraj.ac.in")

@app.route('/colleges/lnctsopindore')
def lnctsopindore():
    return redirect("https://lnctsopindore.in")

@app.route('/colleges/lnctworldschools')
def lnctworldschools():
    return redirect("https://lnctworldschools.com")

@app.route('/colleges/lnctguru')
def lnctguru():
    return redirect("https://lnctguru.com")

@app.route('/colleges/lnayurvedcollege')
def lnayurvedcollege():
    return redirect("https://lnayurvedcollege.com")

# -------------------- 🟠 Company Routes --------------------

@app.route('/Company/jayantjaggery')
def jayantjaggery():
    return redirect("https://jayantjaggery.com")

@app.route('/Company/kalchuricontractors')
def kalchuricontractors():
    return redirect("https://kalchuricontractors.ltd")

@app.route('/Company/parvatisweetners')
def parvatisweetners():
    return redirect("https://parvatisweetners.co.in")

@app.route('/vitamax')
def vitamax():
    return redirect("https://vitamax.co.in")

@app.route('/Company/dabracobrew')
def dabracobrew():
    return redirect("https://dabracobrew.com")

@app.route('/Company/jpsbilaspur')
def jpsbilaspur():
    return redirect("https://jpsbilaspur.com")

@app.route('/Company/ananjay')
def ananjay():
    return redirect("https://ananjay.co.in")

@app.route('/Company/ananjaypharma')
def ananjaypharma():
    return redirect("https://ananjaypharma.co.in")

@app.route('/Company/clchomeopathy')
def clchomeopathy():
    return redirect("https://clchomeopathy.in")






@app.route('/contact')
def contact():
    return jsonify({"page": "Contact", "content": "Get in touch with LNCT."})

# --------------------------------

@app.route('/explore-campus')
def explore_campus():
    return redirect("https://lnct.ac.in/explore-campus")

# @app.route('/apply-now')
# def apply_now():
@app.route('/signin',methods=["POST","GET"])
def Signin():
    if request.method=="POST":
        
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        data=signin(user_name,user_password)
        
        if data==False:
            return render_template('signin.html',error="error while signing in")
        else:
            return redirect('/')
    
    else:
        return render_template('signin.html')
    

@app.route('/login',methods=["POST","GET"])
def Login():
    if request.method=="POST":
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        data=login(user_name, user_password)
        
        if data==False:
            return render_template('login.html', error="Credintials not match")
        else:
            return redirect('/')
        
    else:
        return render_template('login.html')
    
    
# -------------------------?
@app.route('/api/admission')
def admission():
    return jsonify({"title": "Admission", "info": "Admission process and requirements."})

@app.route('/api/courses')
def courses():
    return jsonify({"courses": ["B.Tech", "M.Tech", "MBA", "MCA", "Diploma"]})

@app.route('/api/tour')
def campus_tour():
    return jsonify({"title": "Campus Tour", "video_link": "https://youtube.com/lnct-tour"})

@app.route('/api/facilities')
def facilities():
    return jsonify({"facilities": ["Hostel", "Library", "Labs", "Sports", "Cafeteria"]})

if __name__=="__main__":
    serve(app,host='0.0.0.0', port=2000)

