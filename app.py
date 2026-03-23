from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import sys
from django.conf import settings


settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='demo-secret',
    ALLOWED_HOSTS=['*'],
)


def home(request):
    html = """
    <html>
        <head>
            <title>CI/CD Demo</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    height: 100vh;
                    background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReFonU1eFqPkrPY7fVFGJg_BFVNFg05sHiRg&s');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: Arial, sans-serif;
                }

                .overlay {
                    background-color: rgba(0, 0, 0, 0.6);
                    padding: 40px;
                    border-radius: 15px;
                    text-align: center;
                }

                h1 {
                    color: #00ffcc;
                    font-size: 40px;
                }

                p {
                    color: #ffffff;
                    font-size: 20px;
                }

                .footer {
                    margin-top: 20px;
                    color: #ccc;
                }
            </style>
        </head>
        <body>
            <div class="overlay">
                <h1>🚀 Welcome to CI-CD Pipeline Setup using GitHub Actions</h1>
                <p>This is a Django web app deployed using CI/CD pipeline</p>
                <p class="footer">Pipeline Ready ✔</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path('', home),
]


if __name__ == '__main__':
    execute_from_command_line([sys.argv[0], 'runserver', '0.0.0.0:8000'])