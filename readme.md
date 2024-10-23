Initialize the Database using: flask --app hiverbee init-db

Start the app in debug using: flask --app hiverbee run 

Initalize the Databse on Pythonanywhere: export FLASK_APP=":create_app"
                                        flask shell
                                        from hiberbee import db
                                        db.init_db()