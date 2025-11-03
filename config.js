// Project Chimera - Main Configuration
// WARNING: DO NOT COMMIT THIS FILE WITH KEYS

const config = {
  projectName: "Project Chimera",
  database: {
    host: "dev-server-01.nextgen.io",
    port: 5432,
    user: "chimera_admin"
  },
  aws: {
    accessKeyId: "",
    secretAccessKey: "",
    region: "us-east-1"
  }
};

module.exports = config;
