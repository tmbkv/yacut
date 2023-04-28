from flask import jsonify, request
from urllib.parse import urljoin

from . import app, db
from . error_handlers import InvalidAPIUsage
from . models import URLMap
from . utils import check, get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_short():
    base_url = request.url_root
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    original = data.get('url')
    if not original:
        raise InvalidAPIUsage("\"url\" является обязательным полем!")
    custom_id = data.get('custom_id')
    if custom_id is not None:
        if len(custom_id) > 16 or not check(custom_id):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)
        elif URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
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
            "url": urlmap.original,
            'short_link': urljoin(base_url, custom_id)
        }
    ), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify({'url': url.original}), 200
    raise InvalidAPIUsage('Указанный id не найден', 404)