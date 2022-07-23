import "./Footer.css";
import Typography from "@mui/material/Typography";
import Link from "@mui/material/Link";
export default function FooterCpt() {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
    >
      {"Copyright © "}
      <Link color="inherit" href="https://github.com/toandaominh1997">
        toandaominh1997
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}