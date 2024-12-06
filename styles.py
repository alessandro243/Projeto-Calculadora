import qdarkstyle
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)
 
qss = f"""
    QPushButton[cssClass="numberButton"] {{
        color: #fff;
        background: #009ACD;
        border-radius: 5px;}}

    QPushButton[cssClass="numberButton"]:hover {{
        color: #fff;
        background: #00688B;
    }}
    QPushButton[cssClass="numberButton"]:pressed {{
        color: #fff;
        background: #004C70;
    }}

    QPushButton[cssClass="OButton"] {{
        color: #fff;
        background: #2E8B57;
    }}

    QPushButton[cssClass="OButton"]:hover {{
        color: #fff;
        background: #228B22;
    }}
    QPushButton[cssClass="OButton"]:pressed {{
        color: #fff;
        background: #006400;
    }}

    QPushButton[cssClass="HButton"] {{
        color: #fff;
        background: #FEA610;  /* Laranja (fundo normal) */
        border-radius: 17px; /* Borda arredondada para tornar o botão redondo */
    }}

    QPushButton[cssClass="HButton"]:hover {{
        background: #E28000;  /* Laranja mais escuro (hover) */
    }}

    QPushButton[cssClass="HButton"]:pressed {{
        background: #8D4925;  /* Laranja escuro (pressionado) */
    }}

    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""
 
 
def setupTheme(app):
    # Aplicar o estilo escuro do qdarkstyle
    style_ = qdarkstyle.load_stylesheet_pyside6()
    plus = style_ + qss
    # Sobrepor com o QSS personalizado para estilização adicional
    app.setStyleSheet(style_ + qss)