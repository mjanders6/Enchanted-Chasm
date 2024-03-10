import json

class back_end:
    def __init__(self):
        pass

    # Get json file data
    @staticmethod
    def get_data(db_file):
        with open(db_file) as json_file:
            # Reading from json file
            db = json.load(json_file)
            return db
    # Save json file data
    @staticmethod
    # save data
    def save_data(file, db):
        with open(file, 'w') as json_file_out:
            json.dump(db, json_file_out)

    # read in game board file and save to the MASTER_BOARD list in the db and save the file
    @staticmethod
    def init_board(file, json_file):
        db = back_end.get_data(json_file)

        with open(file, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Split the line into fields based on whitespace
                fields = line.strip().split()
                db['MASTER_BOARD'].append(fields)
            file.close()
        back_end.save_data(json_file, db)

    # read in


# initialize file and database
file = "chasmDB.json"
game_file = 'TheCave.txt'
db = back_end.get_data(file)

# db['MASTER_BOARD'].append([1,2,3,4,5])
# back_end.save_data(file, db)



