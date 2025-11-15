import { useState } from "react";
import styles from "./Login.module.css";

export const Login = ({ onLogin }) => {
  const [email, setEmail] = useState("demo@rotahunter.com");
  const [senha, setSenha] = useState("senha-demo");

  const handleSubmit = (event) => {
    event.preventDefault();
    onLogin({ email, senha });
  };

  return (
    <div className={styles.page}>
      <form className={styles.card} onSubmit={handleSubmit}>
        <h2 className={styles.title}>Rota Hunter</h2>
        <p className={styles.subtitle}>Inteligência Comercial com DNA 100% brasileiro</p>
        <div className={styles.field}>
          <label>E-mail corporativo</label>
          <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" required />
        </div>
        <div className={styles.field}>
          <label>Senha</label>
          <input value={senha} onChange={(e) => setSenha(e.target.value)} type="password" required />
        </div>
        <button className={styles.button} type="submit">
          Entrar
        </button>
        <p style={{ marginTop: 24, fontSize: "0.85rem", color: "var(--cinza-claro)" }}>
          ROTA HUNTER – <span className={styles.highlight}>Inteligência Comercial</span>
        </p>
      </form>
    </div>
  );
};
