import { NavLink, useLocation } from "react-router-dom";
import styles from "./Layout.module.css";

const navItems = [
  { label: "Dashboard", path: "/dashboard" },
  { label: "Hunter", path: "/hunter" },
  { label: "CRM", path: "/crm" },
  { label: "WhatsApp", path: "/whatsapp" },
  { label: "Templates", path: "/templates" },
  { label: "IA", path: "/ia" },
  { label: "Configurações", path: "/configuracoes" },
];

export const Layout = ({ children, usuario, onLogout }) => {
  const location = useLocation();

  return (
    <div className={styles.wrapper}>
      <aside className={styles.sidebar}>
        <div className={styles.logo}>
          ROTA <span>HUNTER</span>
          <div style={{ fontSize: "0.7rem", letterSpacing: "0.3em", marginTop: 4 }}>IA COMERCIAL</div>
        </div>
        <nav className={styles.navList}>
          {navItems.map((item) => (
            <NavLink key={item.path} to={item.path} className={`${styles.navItem} ${location.pathname === item.path ? styles.navItemActive : ""}`}>
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main className={styles.main}>
        <div className={styles.topBar}>
          <div>
            <h1 style={{ fontFamily: "var(--fonte-titulo)", margin: 0, fontSize: "1.4rem" }}>Painel Estratégico</h1>
            <p style={{ color: "var(--cinza-claro)", margin: "6px 0 0" }}>Ambiente totalmente local</p>
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <div className={styles.userCard}>
              <strong>{usuario?.nome}</strong>
              <span>{usuario?.email}</span>
            </div>
            <button className={styles.logoutBtn} onClick={onLogout}>
              Sair
            </button>
          </div>
        </div>
        <div className={styles.content}>{children}</div>
      </main>
    </div>
  );
};
