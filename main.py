from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail


app = Flask(__name__)
app.secret_key = 'the-random-string'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/mylibrary"
app.config.update(
    MAIL_SERVER = '', #smtp.gmail.com
    MAIL_PORT = '', #465
    MAIL_USE_SSL = True,
    MAIL_USERNAME = '',
    MAIL_PASSWORD = ''
)
mail = Mail(app)

db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    Phone_no = db.Column(db.String(20), nullable=False)
    Message = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(120), nullable=False)

class Biography(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Art(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Children(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Fantacy(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class History(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Medicine(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Music(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Mystory(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Plays(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False) 
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Recipies(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Religion(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)

class Romance(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120), nullable=False)


@app.route("/")
def home():
    return render_template('home.html')


#book routes

@app.route("/biography-books")
def readbio():
    posts = Biography.query.filter_by().all()
    return render_template('biography-books.html', posts=posts)

@app.route("/biography-books/<string:book_slug>", methods=['GET'])
def readbiobook(book_slug):
    book = Biography.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/art-books")
def readart():
    posts = Art.query.filter_by().all()
    return render_template('art-books.html', posts=posts)

@app.route("/art-books/<string:book_slug>", methods=['GET'])
def readartbook(book_slug):
    book = Art.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/children-books")
def readchild():
    posts = Children.query.filter_by().all()
    return render_template('children-books.html', posts=posts)

@app.route("/children-books/<string:book_slug>", methods=['GET'])
def readchildbook(book_slug):
    book = Children.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/fantacy-books")
def readfantacy():
    posts = Fantacy.query.filter_by().all()
    return render_template('fantacy-books.html', posts=posts)

@app.route("/fantacy-books/<string:book_slug>", methods=['GET'])
def readfantacybook(book_slug):
    book = Fantacy.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/history-books")
def readhistory():
    posts = History.query.filter_by().all()
    return render_template('history-books.html', posts=posts)

@app.route("/history-books/<string:book_slug>", methods=['GET'])
def readhistorybook(book_slug):
    book = History.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/medicine-books")
def readmedicine():
    posts = Medicine.query.filter_by().all()
    return render_template('medicine-books.html', posts=posts)

@app.route("/medicine-books/<string:book_slug>", methods=['GET'])
def readmedicinebook(book_slug):
    book = Medicine.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/music-books")
def readmusic():
    posts = Music.query.filter_by().all()
    return render_template('music-books.html', posts=posts)

@app.route("/music-books/<string:book_slug>", methods=['GET'])
def readmusicbook(book_slug):
    book = Music.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/mystory-books")
def readmystory():
    posts = Mystory.query.filter_by().all()
    return render_template('mystory-books.html', posts=posts)

@app.route("/mystory-books/<string:book_slug>", methods=['GET'])
def readmystorybook(book_slug):
    book = Mystory.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/plays-books")
def readplays():
    posts = Plays.query.filter_by().all()
    return render_template('plays-books.html', posts=posts)

@app.route("/plays-books/<string:book_slug>", methods=['GET'])
def readplaysbook(book_slug):
    book = Plays.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/reciepy-books")
def readrecipy():
    posts = Recipies.query.filter_by().all()
    return render_template('recipies-books.html', posts=posts)

@app.route("/reciepy-books/<string:book_slug>", methods=['GET'])
def readrecipybook(book_slug):
    book = Recipies.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/religion-books")
def readreligion():
    posts = Religion.query.filter_by().all()
    return render_template('religion-books.html', posts=posts)

@app.route("/religion-books/<string:book_slug>", methods=['GET'])
def readreligionbook(book_slug):
    book = Religion.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)

@app.route("/romantic-books")
def readromantic():
    posts = Romance.query.filter_by().all()
    return render_template('romantic-books.html', posts=posts)

@app.route("/romantic-books/<string:book_slug>", methods=['GET'])
def readromanticbook(book_slug):
    book = Romance.query.filter_by(slug=book_slug).first()
    return render_template('book.html', post=book)
#end of book routes


@app.route("/login", methods=['GET', 'POST'])
def login():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        return render_template('dash.html')

    if (request.method == 'POST'):
        # redirect to dashboard*****************************************************************
        username = request.form.get('email')
        password =request.form.get('password')
        if (username == "suraj@gmail.com" and password == "getitnow"):
            session['user'] = username
            return render_template('dash.html')
    
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/login')

@app.route("/bioedit")  #editing routes start**************************************
def bioedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Biography.query.all()
        return render_template('dashboard.html', posts=posts)
    return render_template('dashboard.html')
    

@app.route("/bioedit/<string:sno>", methods=['GET', 'POST'])
def bioedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Biography(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/bioedit')

            else:
                post = Biography.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/bioedit')
        post = Biography.query.filter_by(sno=sno).first()
        return render_template('edit.html', post = post, sno=sno)

@app.route("/biodelete/<string:sno>", methods=['GET', 'POST'])
def biodelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Biography.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/bioedit')

@app.route("/artedit")  #editing art routes start**************************************
def artedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Art.query.all()
        return render_template('dashboard1.html', posts=posts)
    return render_template('dashboard1.html')
    

@app.route("/artedit/<string:sno>", methods=['GET', 'POST'])
def artedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Art(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/artedit')

            else:
                post = Art.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/artedit')
        post = Art.query.filter_by(sno=sno).first()
        return render_template('edit1.html', post = post, sno=sno)

@app.route("/artdelete/<string:sno>", methods=['GET', 'POST'])
def artdelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Art.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/artedit')

@app.route("/childedit")  #editing child routes start**************************************
def childedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Children.query.all()
        return render_template('dashboard2.html', posts=posts)
    return render_template('dashboard2.html')
    

@app.route("/childedit/<string:sno>", methods=['GET', 'POST'])
def childedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Children(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/childedit')

            else:
                post = Children.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/childedit')
        post = Children.query.filter_by(sno=sno).first()
        return render_template('edit2.html', post = post, sno=sno)

@app.route("/childdelete/<string:sno>", methods=['GET', 'POST'])
def childdelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Children.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/childedit')

@app.route("/fantacyedit")  #editing child routes start**************************************
def fantacyedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Fantacy.query.all()
        return render_template('dashboard3.html', posts=posts)
    return render_template('dashboard3.html')
    

@app.route("/fantacyedit/<string:sno>", methods=['GET', 'POST'])
def fantacyedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Fantacy(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/fantacyedit')

            else:
                post = Fantacy.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/fantacyedit')
        post = Fantacy.query.filter_by(sno=sno).first()
        return render_template('edit3.html', post = post, sno=sno)

@app.route("/fantacydelete/<string:sno>", methods=['GET', 'POST'])
def fantacydelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Fantacy.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/fantacyedit')

@app.route("/historyedit")  #editing child routes start**************************************
def historyedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = History.query.all()
        return render_template('dashboard4.html', posts=posts)
    return render_template('dashboard4.html')
    

@app.route("/historyedit/<string:sno>", methods=['GET', 'POST'])
def historyedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = History(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/historyedit')

            else:
                post = History.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/historyedit')
        post = History.query.filter_by(sno=sno).first()
        return render_template('edit4.html', post = post, sno=sno)

@app.route("/historydelete/<string:sno>", methods=['GET', 'POST'])
def historydelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = History.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/historyedit')

@app.route("/medicineedit")  #editing child routes start**************************************
def medicineedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Medicine.query.all()
        return render_template('dashboard5.html', posts=posts)
    return render_template('dashboard5.html')
    

@app.route("/medicineedit/<string:sno>", methods=['GET', 'POST'])
def medicineedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Medicine(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/medicineedit')

            else:
                post = Medicine.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/medicineedit')
        post = Medicine.query.filter_by(sno=sno).first()
        return render_template('edit5.html', post = post, sno=sno)

@app.route("/medicinedelete/<string:sno>", methods=['GET', 'POST'])
def medicinedelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Medicine.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/medicineedit')

@app.route("/musicedit")  #editing child routes start**************************************
def musicedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Music.query.all()
        return render_template('dashboard6.html', posts=posts)
    return render_template('dashboard6.html')
    

@app.route("/musicedit/<string:sno>", methods=['GET', 'POST'])
def musicedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Music(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/musicedit')

            else:
                post = Music.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/musicedit')
        post = Music.query.filter_by(sno=sno).first()
        return render_template('edit6.html', post = post, sno=sno)

@app.route("/musicdelete/<string:sno>", methods=['GET', 'POST'])
def musicdelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Music.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/musicedit')

@app.route("/mystoryedit")  #editing child routes start**************************************
def mystoryedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Mystory.query.all()
        return render_template('dashboard7.html', posts=posts)
    return render_template('dashboard7.html')
    

@app.route("/mystoryedit/<string:sno>", methods=['GET', 'POST'])
def mystoryedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Mystory(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/mystoryedit')

            else:
                post = Mystory.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/mystoryedit')
        post = Mystory.query.filter_by(sno=sno).first()
        return render_template('edit7.html', post = post, sno=sno)

@app.route("/mystorydelete/<string:sno>", methods=['GET', 'POST'])
def mystorydelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Mystory.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/mystoryedit')

@app.route("/playsedit")  #editing child routes start**************************************
def playsedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Plays.query.all()
        return render_template('dashboard8.html', posts=posts)
    return render_template('dashboard8.html')
    

@app.route("/playsedit/<string:sno>", methods=['GET', 'POST'])
def playsedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Plays(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/playsedit')

            else:
                post = Plays.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/playsedit')
        post = Plays.query.filter_by(sno=sno).first()
        return render_template('edit8.html', post = post, sno=sno)

@app.route("/playsdelete/<string:sno>", methods=['GET', 'POST'])
def playdelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Plays.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/playsedit')


@app.route("/recipyedit")  #editing child routes start**************************************
def recipyedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Recipies.query.all()
        return render_template('dashboard9.html', posts=posts)
    return render_template('dashboard9.html')
    

@app.route("/recipyedit/<string:sno>", methods=['GET', 'POST'])
def recipyedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Recipies(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/recipyedit')

            else:
                post = Recipies.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/recipyedit')
        post = Recipies.query.filter_by(sno=sno).first()
        return render_template('edit9.html', post = post, sno=sno)

@app.route("/recipydelete/<string:sno>", methods=['GET', 'POST'])
def recipydelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Recipies.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/recipyedit')


@app.route("/religionedit")  #editing child routes start**************************************
def religionedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Religion.query.all()
        return render_template('dashboard10.html', posts=posts)
    return render_template('dashboard10.html')
    

@app.route("/religionedit/<string:sno>", methods=['GET', 'POST'])
def religionedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Religion(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/religionedit')

            else:
                post = Religion.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/religionedit')
        post = Religion.query.filter_by(sno=sno).first()
        return render_template('edit10.html', post = post, sno=sno)

@app.route("/religiondelete/<string:sno>", methods=['GET', 'POST'])
def religiondelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Religion.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/religionedit')

@app.route("/romanticedit")  #editing child routes start**************************************
def romanticedit():
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        posts = Romance.query.all()
        return render_template('dashboard11.html', posts=posts)
    return render_template('dashboard11.html')
    

@app.route("/romanticedit/<string:sno>", methods=['GET', 'POST'])
def romanticedit1(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        if request.method == 'POST':
            edit_title = request.form.get('title')
            edit_slug = request.form.get('slug')
            edit_image = request.form.get('image') 
            edit_content = request.form.get('content')

            if sno=='0':
                post = Romance(title = edit_title, slug = edit_slug,image = edit_image, content = edit_content)
                db.session.add(post)
                db.session.commit()
                return redirect('/romanticedit')

            else:
                post = Romance.query.filter_by(sno=sno).first()
                post.title = edit_title
                post.slug = edit_slug
                post.image = edit_image
                post.content = edit_content
                
                db.session.commit()
                return redirect('/romanticedit')
        post = Romance.query.filter_by(sno=sno).first()
        return render_template('edit11.html', post = post, sno=sno)

@app.route("/romanticdelete/<string:sno>", methods=['GET', 'POST'])
def romanticdelete(sno):
    if ('user' in session and session['user'] == "suraj@gmail.com"):
        post = Romance.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/romanticedit')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    if (request.method=='POST') :
        # adding entry to the database

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name, email=email, Phone_no=phone, Message=message, time=datetime.now())

        db.session.add(entry)
        db.session.commit()

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=['wadikarsuraj02@gmail.com'],
                          body=message + '\n' + 'The phone no. of '+ name + ' is '+ phone,
                          )
        
    return render_template('contact.html')


app.run(debug=True)