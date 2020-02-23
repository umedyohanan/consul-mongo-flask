db.createUser(
    {
        user: "admin",
        pwd: "Admin123",
        roles: [
            {
                role: "userAdminAnyDatabase",
                db: "admin"
            }
        ]
    }
);
