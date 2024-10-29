from flask_wtf import FlaskForm
from wtforms import SearchField, SelectField, FileField, StringField, SubmitField, BooleanField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import Length, DataRequired, Optional
from flask_wtf.file import FileAllowed, FileRequired


class NewCard(FlaskForm):
    name=StringField(
        'Наименование карточки',
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    image=FileField('Изоюражение',
                    validators=[FileRequired(message="Поле не может быть пустым"),
                    FileAllowed(['jpg', 'jpeg', 'png', 'ico', 'avif'], message="Неверный формат файла")])
    adress=StringField(
        'Ссылка на страницу',
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    content=StringField(
        'Основные слова',
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    submit=SubmitField('Добавить данные')
class GetSummary(FlaskForm):
    lastname = StringField(
        'Фамилия',
        validators=[DataRequired(message='Обязательно к заполнению')]
    )
    name = StringField(
        'Имя',
        validators=[DataRequired(message='Обязательно к заполнению')]
    )
    second_name = StringField(
        'Отчество',
        validators=[DataRequired(message='Обязательно к заполнению')]
    )
    phone_number = StringField(
        'Номер телефона',
        validators=[DataRequired(message='Обязательно к заполнению')]
    )
    
    education = SelectField(
        'Образование',
        validators=[DataRequired(message='Обязательно к заполнению')],
                    choices=[('ВО'),('СПО') ]
    )
    have_Russian_pasport = BooleanField(default=False, validators=[DataRequired(message='Обязательно к заполнению')])
    dont_use_drugs = BooleanField(default=False, validators=[DataRequired(message='Обязательно к заполнению')])
    accept_prov = BooleanField(default=False)
    submit = SubmitField(name='Отправить данные', default=False, validators=[DataRequired(message='Обязательно к заполнению')])

    
class GetAppeal(FlaskForm):
    fio=StringField(
        'Ф.И.О', 
        validators=[DataRequired(message='Обязательно к заполнению')])
    email_visitor=StringField('Email',
      validators=[DataRequired(message='Обязательно к заполнению')]                        )
    text_letter=TextAreaField('Текст',
        validators=[DataRequired(message='Обязательно к заполнению')])
    submit=SubmitField(name='Отправить',default=False)

class AddQuestion(FlaskForm):
    fio=StringField(
        'Ф.И.О', 
        validators=[DataRequired(message='Обязательно к заполнению')])
    email_visitor=StringField('Email',
      validators=[DataRequired(message='Обязательно к заполнению')]                        )
    text_letter=TextAreaField('Текст',
        validators=[DataRequired(message='Обязательно к заполнению')])
    submit=SubmitField(name='Отправить',default=False)

class AddNews(FlaskForm):
    name_news=StringField(
        'Наименование новости',
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    text_news=TextAreaField(
        'Текст новости',
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    url=StringField(
        'Url адрес',
         validators=[DataRequired(message="Поле не может быть пустым")]
    )
    date_news=DateTimeField(
        'Время публикации новости',
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    submit=SubmitField("Добавить новость")
class SearchForm(FlaskForm):
    searched=StringField(
        "Поиск",
        validators=[DataRequired(message="Поле не может быть пустым")]
    )
    submit_search=SubmitField("")
class Login_Svo_Sequrity(FlaskForm):
    username=StringField(validators=[DataRequired(message="Обязательно к заполнению")])
    password=PasswordField(validators=[DataRequired(message="Обязательно к заполнению")])
    submit=SubmitField("Войти")
class RegistrationForm(FlaskForm):
    fio=StringField(validators=[DataRequired(message="Обязательно к заполнению")])
    username=StringField(validators=[DataRequired(message="Обязательно к заполнению")])
    password=PasswordField(validators=[DataRequired(message="Обязательно к заполнению")])
    submit=SubmitField("Зарегестрироваться")

