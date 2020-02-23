db.getSiblingDB('tweeter');

db.createUser(
    {
        user: "dbuser",
        pwd: "dbpwd123",
        roles: [
            {
                role: "readWrite",
                db: "tweets"
            }
        ]
    }
);