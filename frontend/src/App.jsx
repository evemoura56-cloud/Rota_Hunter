import { useMemo, useState } from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Login } from "./pages/Login";
import { Dashboard } from "./pages/Dashboard";
import { Hunter } from "./pages/Hunter";
import { CRM } from "./pages/CRM";
import { WhatsApp } from "./pages/WhatsApp";
import { Templates } from "./pages/Templates";
import { IA } from "./pages/IA";
import { Configuracoes } from "./pages/Configuracoes";

const statusFunil = ["PROSPECTADO", "CONTATADO", "RESPONDEU", "QUALIFICADO", "PROPOSTA", "GANHO", "PERDIDO"];

const leadsSeed = {
  PROSPECTADO: [
    { id: 1, nome: "Kratos Digital", setor: "Tecnologia", pwin: 31 },
    { id: 2, nome: "Magma Foods", setor: "Alimentos", pwin: 22 },
  ],
  CONTATADO: [{ id: 3, nome: "Artemis Labs", setor: "Saúde", pwin: 48 }],
  RESPONDEU: [{ id: 4, nome: "Pulsar Energia", setor: "Energia", pwin: 55 }],
  QUALIFICADO: [{ id: 5, nome: "Aurora Retail", setor: "Varejo", pwin: 62 }],
  PROPOSTA: [{ id: 6, nome: "Neon Logistics", setor: "Logística", pwin: 71 }],
  GANHO: [{ id: 7, nome: "Flux Mining", setor: "Mineração", pwin: 94 }],
  PERDIDO: [{ id: 8, nome: "Boreal Agro", setor: "Agro", pwin: 12 }],
};

const empresasSeed = [
  { id: 11, nome: "Red Senses", setor: "Moda", regiao: "SP", site: "redsenses.com", prioridade: "Alta" },
  { id: 12, nome: "PrimeSteel", setor: "Indústria", regiao: "MG", site: "primesteel.com", prioridade: "Média" },
];

const templatesSeed = [
  { id: 1, nome: "Apresentação", assunto: "Nova inteligência de fornecedores", corpo: "Olá {{nome}}, podemos falar sobre homologação?" },
  { id: 2, nome: "Follow-up", assunto: "Confirmação de proposta", corpo: "{{nome}}, deixei uma proposta disponível ontem." },
];

const contatosSeed = [
  { id: 1, nome: "Patrícia Lopes", cargo: "Compras", empresa: "Aurora Retail", whatsapp: "551198887766" },
  { id: 2, nome: "Julio Cesar", cargo: "Operações", empresa: "Neon Logistics", whatsapp: "551197887755" },
];

const iaSeed = [
  { id: 1, empresa: "Aurora Retail", setor: "Varejo", pwin: 86, motivo: "Engajamento alto" },
  { id: 2, empresa: "Pulsar Energia", setor: "Energia", pwin: 63, motivo: "Resposta rápida" },
  { id: 3, empresa: "Kratos Digital", setor: "Tecnologia", pwin: 54, motivo: "Abertura de e-mail alta" },
];

export default function App() {
  const [usuario, setUsuario] = useState(() => {
    const raw = localStorage.getItem("rota_usuario");
    return raw ? JSON.parse(raw) : null;
  });
  const [empresas, setEmpresas] = useState(empresasSeed);
  const [leads, setLeads] = useState(leadsSeed);
  const [templates, setTemplates] = useState(templatesSeed);
  const [iaRegistros, setIaRegistros] = useState(iaSeed);

  const handleLogin = ({ email }) => {
    const perfil = { nome: "Analista Rota Hunter", email };
    localStorage.setItem("rota_usuario", JSON.stringify(perfil));
    setUsuario(perfil);
  };

  const handleLogout = () => {
    localStorage.removeItem("rota_usuario");
    setUsuario(null);
  };

  const handleDiscover = ({ setor, regiao, keywords }) => {
    const nova = {
      id: Date.now(),
      nome: `${setor} Insights ${Math.floor(Math.random() * 90)}`,
      setor,
      regiao,
      site: `${setor.toLowerCase().replace(/ /g, "")}.com`,
      prioridade: keywords.includes("dados") ? "Alta" : "Média",
    };
    setEmpresas((prev) => [nova, ...prev]);
  };

  const handleKanbanMove = (source, destination) => {
    if (source.droppableId === destination.droppableId && source.index === destination.index) return;
    setLeads((prev) => {
      const copy = JSON.parse(JSON.stringify(prev));
      const [moved] = copy[source.droppableId].splice(source.index, 1);
      copy[destination.droppableId].splice(destination.index, 0, moved);
      return copy;
    });
  };

  const handleCreateLead = ({ nome, setor, status }) => {
    setLeads((prev) => ({
      ...prev,
      [status]: [{ id: Date.now(), nome, setor, pwin: 20 }, ...prev[status]],
    }));
  };

  const handleTemplateSave = (templateAtualizado) => {
    setTemplates((prev) => prev.map((tpl) => (tpl.id === templateAtualizado.id ? templateAtualizado : tpl)));
  };

  const handleTreinarIA = () => {
    setIaRegistros((prev) => prev.map((item) => ({ ...item, pwin: Math.min(99, item.pwin + 1) })));
  };

  const dashboardData = useMemo(() => {
    const totalLeads = statusFunil.reduce((acc, status) => acc + leads[status].length, 0);
    const ganho = leads.GANHO.length;
    const taxaConversao = totalLeads ? Math.round((ganho / totalLeads) * 100) : 0;
    return {
      kpis: [
        { label: "Leads ativos", value: totalLeads },
        { label: "Taxa conversão", value: `${taxaConversao}%`, tag: "Últimos 30 dias" },
        { label: "Leads quentes", value: leads.PROPOSTA.length + leads.GANHO.length },
        { label: "Emails enviados", value: "214", tag: "24h" },
      ],
      charts: {
        pizza: Object.entries(leads).map(([nome, lista]) => ({ nome, valor: lista.length || 1 })),
        barras: Object.entries(leads).map(([nome, lista]) => ({ nome, valor: lista.length })),
        linha: [1, 2, 3, 4, 5, 6].map((dia) => ({ dia: `S${dia}`, valor: Math.round(Math.random() * 60) + 10 })),
        velocidade: [
          { nome: "Contato", dias: 3 },
          { nome: "Qualificação", dias: 6 },
          { nome: "Proposta", dias: 4 },
          { nome: "Fechamento", dias: 2 },
        ],
      },
    };
  }, [leads]);

  if (!usuario) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <Layout usuario={usuario} onLogout={handleLogout}>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<Dashboard kpis={dashboardData.kpis} charts={dashboardData.charts} />} />
        <Route path="/hunter" element={<Hunter empresas={empresas} onDiscover={handleDiscover} />} />
        <Route path="/crm" element={<CRM colunas={leads} onMove={handleKanbanMove} onCreate={handleCreateLead} />} />
        <Route path="/whatsapp" element={<WhatsApp contatos={contatosSeed} />} />
        <Route path="/templates" element={<Templates templates={templates} onSave={handleTemplateSave} />} />
        <Route path="/ia" element={<IA registros={iaRegistros} onTreinar={handleTreinarIA} />} />
        <Route path="/configuracoes" element={<Configuracoes dados={[{ label: "Usuário", valor: usuario.nome }, { label: "E-mail", valor: usuario.email }, { label: "Modo IA", valor: "Local" }]} />} />
        <Route path="*" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </Layout>
  );
}
