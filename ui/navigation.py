# ------IMPORTS------------------------------------------
import sys
import os
from PyQt6.QtWidgets import  QPushButton, QMessageBox, QLabel
from db_session import DBSession
from typing import Optional
from login import Login_UI
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# ---------------------------------------------------------

# ---------NAVIGATION_UI CLASS--------------------------------
class Navigation_UI:
    # List of objects in .ui file related to this module
    admin_id                : QLabel
    admin_name              : QLabel
    
    home_btn                : QPushButton
    open_btn                : QPushButton
    search_btn              : QPushButton
    add_btn                 : QPushButton
    
    logout_btn              : QPushButton
    
    def __init__(self, ui, db_session: DBSession):
        self.ui         = ui
        self.db_session = db_session
        
        # List of buttons in the navigation bar
        self.buttons_nav = [
            self.ui.home_btn,
            self.ui.add_btn,
            self.ui.search_btn,
            self.ui.open_btn,
        ]

        # Add page
        self.ui.add_btn.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentWidget(self.ui.add_page))
        # Search page
        self.ui.search_btn.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentWidget(self.ui.search_page))
        # Open page
        self.ui.open_btn.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentWidget(self.ui.open_page))
        # Home page
        self.ui.home_btn.clicked.connect(lambda: self.ui.main_stackedWidget.setCurrentWidget(self.ui.home_page))
        
        # Log out
        self.ui.logout_btn.clicked.connect(self.comfirmLogOut)
        
        # Save the last clicked button
        self.lastClickedNavButton: Optional[QPushButton] = None
        
        for button in self.buttons_nav:
            button.clicked.connect(lambda checked, b=button: self.navigationButtonClicked(b))
        
    def comfirmLogOut(self):
        
        reply = QMessageBox.question(self.ui, 'Message', "Are you sure you want to log out?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.logOut()
        
    def logOut(self):
        
        self.ui.close()
        
        self.login_window = Login_UI(self.db_session)
        self.login_window.show()
    
    def navigationButtonClicked(self, button):
        if self.lastClickedNavButton is not None:
            self.lastClickedNavButton.setStyleSheet("""
                QPushButton{
                    border: 2px solid black;
                    color: black;
                }
                QPushButton:hover{
                    border: 2px solid #560bad;
                    color: #560bad;
                }
            """)
            self.lastClickedNavButton.setDisabled(False)
        
        button.setStyleSheet("""
            QPushButton{
                border: 2px solid grey;
                color: grey;
            }
        """)
        button.setDisabled(True)
        
        self.lastClickedNavButton = button
    
    
    
    

    
    