from flask import Flask, jsonify, render_template, request, redirect
from Database import *
from POJO.Pojoes import *

app = Flask(__name__)
UserProfile_ = UserProfile()


# Страница Главная
@app.route('/home')
def home():
    # Ваш код для получения информации о последних обновлениях
    updates = [
        {"id": 1, "title": "Обновление 1", "description": "Описание обновления 1"},
        {"id": 2, "title": "Обновление 2", "description": "Описание обновления 2"}
    ]
    return render_template('home.html', updates=updates)


# Страница Профиль
@app.route('/profile')
def profile():
    # Ваш код для получения информации о пользователе
    user_info = {
        "id": UserProfile_.id,
        "login": UserProfile_.user_login,
        "password": UserProfile_.user_password,
        "first_name": UserProfile_.first_name,
        "last_name": UserProfile_.last_name,
        "phone": UserProfile_.phone,
        "role": UserProfile_.access_key
    }

    # Ваш код для получения информации об отчетах (пример)
    reports = [
        {"id": 1, "date": "2024-02-05", "substance_id": 1, "user_id": 123,
         "affected_area": [10.5, 20.3, 15.8], "average_population_density": 50, "affected": [5, 8, 3]},
        {"id": 2, "date": "2024-02-04", "substance_id": 2, "user_id": 123,
         "affected_area": [8.2, 12.7, 17.4], "average_population_density": 60, "affected": [3, 6, 2]}
    ]
    return render_template('profile.html', user=user_info, reports=reports)


# Страница Прогнозирования
@app.route('/forecast')
def forecast():
    return render_template('forecast.html')


# Обработка формы для перехода между страницами
@app.route('/navigate', methods=['POST'])
def navigate():
    page = request.form['page']
    if page == 'home':
        return home()
    elif page == 'profile':
        return profile()
    elif page == 'forecast':
        return forecast()
    else:
        return 'Page not found'


@app.route('/start_forecast', methods=['POST'])
def start_forecast():
    spread_type = request.form['spread_type']
    pressure = request.form['pressure']
    temperature = request.form['temperature']
    wind_direction = request.form['wind_direction']
    substance_pressure = request.form['substance_pressure']
    substance_volume = request.form['substance_volume']
    substance_temperature = request.form['substance_temperature']
    input_method = request.form['input_method']

    # Ваш код для обработки полученных данных и запуска прогнозирования

    return render_template('forecast.html')


# Страница для редактирования профиля
@app.route('/edit_profile')
def edit_profile():
    # Ваш код для получения информации о пользователе
    user_info = {
        "id": UserProfile_.id,
        "login": "user1",
        "password": "example_password",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "123456789",
        "role": "admin"
    }
    return render_template('edit_profile.html', user=user_info)


# Обработка обновления профиля
@app.route('/update_profile', methods=['POST'])
def update_profile():
    # Ваш код для обновления информации о пользователе в базе данных
    # Пример обновления информации о пользователе
    id = request.form['id']
    login = request.form['login']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']

    # Ваш код для обновления данных пользователя

    # После обновления перенаправляем пользователя на страницу профиля
    return redirect('/profile')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global UserProfile_
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        # Здесь можно добавить логику для проверки логина и пароля в базе данных
        buf_arr = get_user_by_login(username)
        print(buf_arr)
        if len(buf_arr) != 0:
            buf = buf_arr[0]
            print(buf)
            buf_user = UserProfile(buf.Id, buf.UserLogin, buf.UserPassword,
                                   buf.FirstName, buf.LastName, buf.Phone, buf.AccessKey)
            print("obj done")
            print(buf_user)
            if buf_user.user_password == password:
                UserProfile_ = buf_user
                return redirect("/home")
            else:
                print("Not corrected password")
        else:
            print("Not corrected login")
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    global UserProfile_
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        phone = request.form['phone']
        activationKey = request.form['activationKey']
        # Здесь можно добавить логику для регистрации пользователя в базе данных
        insert_user(UserProfile(0, username, password, firstName, lastName, phone, activationKey))
        buf = get_user_by_login(username)[0]
        UserProfile_ = UserProfile(buf.Id, buf.UserLogin, buf.UserPassword,
                                   buf.FirstName, buf.LastName, buf.Phone, buf.AccessKey)
        # После успешной регистрации можно перенаправить на другую страницу
        return redirect("/home")
    return render_template('register.html')


# Добавьте соответствующий шаблон edit_profile.html в ваш проект


@app.route('/')
def root():
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
