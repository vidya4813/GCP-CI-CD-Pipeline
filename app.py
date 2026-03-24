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
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f0f8ff;
                }

                h1 {
                    margin-top: 30px;
                    color: green;
                    font-size: 36px;
                }

                .image-container {
                    margin-top: 20px;
                }

                img {
                    width: 100%;
                    height: auto;
                    max-height: 80vh;
                    object-fit: cover;
                }

                .footer {
                    margin-top: 20px;
                    color: gray;
                    font-size: 18px;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Welcome to CI-CD Pipeline Setup using GitHub Actions</h1>

            <div class="image-container">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReFonU1eFqPkrPY7fVFGJg_BFVNFg05sHiRg&s"
                     alt="CI/CD Demo Image">
            </div>

            <p class="footer">Pipeline Ready ✔.</p>
        </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path('', home),
]


if __name__ == '__main__':
    execute_from_command_line([sys.argv[0], 'runserver', '0.0.0.0:8000'])