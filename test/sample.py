import requests
import hashlib


def send_a_request():
    """
    Before the test, please set the config file.
    """
    with open("./python.html") as html_file:
        html_file_str = html_file.read()

    md5_code = hashlib.md5(html_file_str.encode('utf-8')).hexdigest()
    json_data = {
        "html_page": html_file_str,
        "md5": md5_code,
        "type": "standard",
    }
    response = requests.post("http://127.0.0.1:5000", json=json_data)
    assert response.status_code == 200
    assert response.json().get('status') == 'sucess' 


if __name__ == "__main__":
    send_a_request()
