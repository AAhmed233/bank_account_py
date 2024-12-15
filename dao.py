"""
def findAllTrackScoresByRange():
    try:
        db=cnx.cursor()
        db.execute("SELECT SUM(CASE WHEN trackScore < 50 THEN 1 ELSE 0 END), SUM(CASE WHEN trackScore >= 50 AND trackScore <= 100 THEN 1 ELSE 0 END), SUM(CASE WHEN trackScore > 100 AND trackScore <= 200 THEN 1 ELSE 0 END) , SUM(CASE WHEN trackScore > 200 THEN 1 ELSE 0 END) FROM t_spotify;")
        data=db.fetchall()
        return data
    except my.Error as e :
        print(e)
 
if __name__ == "__main__":
    db=cnx.cursor()
    #db.execute("DELETE FROM t_spotify")
    db.execute(f"INSERT INTO bankaccount VALUES ({500}, {'Checking'}, {0});")
    cnx.commit()


    CREATE TABLE BankAccount (
    id INT AUTO_INCREMENT PRIMARY KEY, -- ID unique et auto-incrémenté
    balance FLOAT NOT NULL,            -- Solde du compte
    accountType ENUM('Saving', 'Checking') NOT NULL, -- Type de compte
    interestRate FLOAT DEFAULT NULL,   -- Taux d'intérêt pour les comptes d'épargne
    transactionCount INT DEFAULT 0     -- Nombre de transactions pour les comptes courants
    );
    
    CREATE TABLE Transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,                     -- ID unique de la transaction
    accountId INT NOT NULL,                                -- ID du compte impliqué
    transactionType ENUM('Deposit', 'Withdraw', 'Transfer') NOT NULL, -- Type de la transaction
    amount FLOAT NOT NULL,                                 -- Montant de la transaction
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,          -- Date et heure de la transaction
    relatedAccountId INT DEFAULT NULL,                    -- ID du compte destinataire pour un transfert
    FOREIGN KEY (accountId) REFERENCES BankAccount(id) ON DELETE CASCADE, -- Relation avec BankAccount
    FOREIGN KEY (relatedAccountId) REFERENCES BankAccount(id) ON DELETE SET NULL -- Relation pour transferts
);


"""
import mysql.connector as my 

# Connexion à la base de données
cnx = my.connect(
    user='root',
    password='',
    host='127.0.0.1',
    port='3306',
    database='db_bank'
)

def insertChekingAccount(values):# value (500, 'Checking', 0)
    try:
        db = cnx.cursor()
        query = "INSERT INTO bankaccount (balance, accountType, transactionCount) VALUES (%s, %s, %s)"
        db.execute(query, values)
        cnx.commit()
    except my.Error as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")

def insertSavingAccount(values):# value (500, 'Saving', 0,5)
    try:
        db = cnx.cursor()
        query = "INSERT INTO bankaccount (balance, accountType, interestRate) VALUES (%s, %s, %s)"
        db.execute(query, values)
        cnx.commit()
    except my.Error as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")

def insertTransaction(values):
    try:
        db = cnx.cursor()
        query = "INSERT INTO transaction (accountId, transactionType, amount, timestamp, relatedAccountId) VALUES (%s, %s, %s, %s, %s)"
        db.execute(query, values)
        cnx.commit()
    except my.Error as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")





