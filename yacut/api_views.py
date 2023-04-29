from http import HTTPStatus
from flask import jsonify, request
from urllib.parse import urljoin

from . error_handlers import InvalidAPIUsage
from . models import URLMap
from . utils import check, get_unique_short_id

from . import app, db, SIZE_SHORT_URL


@app.route('/api/id/', methods=['POST'])
def add_short():
    base_url = request.url_root
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(
            'Отсутствует тело запроса',
            HTTPStatus.BAD_REQUEST
        )
    original = data.get('url')
    if not original:
        raise InvalidAPIUsage(
            '\"url\" является обязательным полем!',
            HTTPStatus.BAD_REQUEST
        )
    custom_id = data.get('custom_id')
    if custom_id is not None:
        if len(custom_id) > SIZE_SHORT_URL or not check(custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
                HTTPStatus.BAD_REQUEST
            )
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(
                f'Имя "{custom_id}" уже занято.',
                HTTPStatus.BAD_REQUEST
            )
    # Без else ошибка. Возможно, что в этом блоке if нет guard block
    else:
        custom_id = get_unique_short_id()
    urlmap = URLMap(
        original=original,
        short=custom_id
    )
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(
        {
            'url': urlmap.original,
            'short_link': urljoin(base_url, custom_id)
        }
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify({'url': url.original}), HTTPStatus.OK
    raise InvalidAPIUsage(
        'Указанный id не найден',
        HTTPStatus.NOT_FOUND
    )