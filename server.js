const http = require("node:http");

const BRANCH = "case/ambiguous:node";
const port = Number(process.env.PORT || 8080);

http
  .createServer((req, res) => {
    const body = JSON.stringify({ branch: BRANCH, lang: "node", path: req.url });
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(body);
  })
  .listen(port, "0.0.0.0", () => console.log(`${BRANCH} listening on ${port}`));
