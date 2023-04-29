from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


MAX_LENGTH_URL = 16


class URLForm(FlaskForm):
    original_link = URLField(
        'Введите оригинальную длинную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Пользовательский вариант',
        validators=[Length(1, MAX_LENGTH_URL), Optional()]
    )
    submit = SubmitField('Создать')