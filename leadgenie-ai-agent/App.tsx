import React, { useState } from "react";
import { ICP, Lead, AppState } from "./types";
import { searchLeads } from "./services/geminiService";
import ICPForm from "./components/ICPForm";
import LeadCard from "./components/LeadCard";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts";

const INITIAL_ICP: ICP = {
  industry: "Enterprise SaaS",
  companySize: "100-1000 employees",
  targetRegion: "EMEA & North America",
  painPoints: "Legacy system migration, AI implementation gaps",
  technologies: "Salesforce, Snowflake, Kubernetes",
};

const App: React.FC = () => {
  const [state, setState] = useState<AppState>({
    icp: INITIAL_ICP,
    leads: [],
    isSearching: false,
    searchQuery: "AI infrastructure companies series B",
  });

  const [error, setError] = useState<string | null>(null);

  const handleSearch = async () => {
    if (!state.searchQuery.trim()) return;

    setState((prev) => ({ ...prev, isSearching: true, leads: [] }));
    setError(null);

    try {
      const results = await searchLeads(state.searchQuery, state.icp);
      setState((prev) => ({ ...prev, leads: results, isSearching: false }));
    } catch (err) {
      console.error(err);
      setError("Failed to fetch leads. Research pipeline interrupted.");
      setState((prev) => ({ ...prev, isSearching: false }));
    }
  };

  const handleStatusChange = (
    id: string,
    status: "shortlisted" | "rejected"
  ) => {
    setState((prev) => ({
      ...prev,
      leads: prev.leads.map((lead) =>
        lead.id === id ? { ...lead, status } : lead
      ),
    }));
  };

  const statsData = [
    {
      name: "Queue",
      count: state.leads.filter((l) => l.status === "new").length,
      color: "#64748b",
    },
    {
      name: "Elite",
      count: state.leads.filter((l) => l.status === "shortlisted").length,
      color: "#818cf8",
    },
    {
      name: "Discard",
      count: state.leads.filter((l) => l.status === "rejected").length,
      color: "#f43f5e",
    },
  ];

  return (
    <div className="min-h-screen pb-12">
      {/* Premium Navigation */}
      <nav className="glass-panel border-b-0 px-8 py-5 sticky top-0 z-50 backdrop-blur-2xl">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 bg-gradient-to-tr from-indigo-600 to-purple-500 rounded-2xl flex items-center justify-center text-white shadow-[0_0_20px_rgba(99,102,241,0.5)]">
              <i className="fas fa-microchip text-2xl"></i>
            </div>
            <div>
              <h1 className="text-2xl font-black text-white tracking-tighter uppercase italic">
                LeadGenie <span className="text-indigo-400">Pro</span>
              </h1>
              <p className="text-[10px] text-indigo-300/60 font-bold tracking-[0.2em]">
                AUTONOMOUS INTELLIGENCE UNIT
              </p>
            </div>
          </div>
          <div className="flex gap-6 items-center">
            <div className="hidden md:block text-right">
              <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">
                Neural Link
              </div>
              <div className="text-xs text-indigo-400 flex items-center gap-2 justify-end font-medium">
                <span className="w-2 h-2 bg-indigo-500 rounded-full animate-pulse shadow-[0_0_8px_#6366f1]"></span>
                STANDBY
              </div>
            </div>
            <div className="h-8 w-[1px] bg-white/10 mx-2"></div>
            <button className="bg-white/5 hover:bg-white/10 text-white px-5 py-2 rounded-xl font-bold transition-all border border-white/10 text-sm tracking-wide">
              ACCOUNT
            </button>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-6 mt-12">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          {/* Left Panel: Control Center */}
          <div className="lg:col-span-4 space-y-8">
            <div className="glass-panel p-8 rounded-3xl overflow-hidden relative">
              <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-600/10 blur-3xl -mr-16 -mt-16"></div>
              <h2 className="text-lg font-bold text-white mb-6 flex items-center gap-3">
                <i className="fas fa-radar text-indigo-500"></i>
                Target Scan
              </h2>
              <div className="space-y-6">
                <div>
                  <label className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-3">
                    Discovery Query
                  </label>
                  <div className="relative group">
                    <input
                      type="text"
                      value={state.searchQuery}
                      onChange={(e) =>
                        setState((prev) => ({
                          ...prev,
                          searchQuery: e.target.value,
                        }))
                      }
                      placeholder="e.g. Cybersecurity firms UK"
                      className="glass-input w-full pl-5 pr-14 py-4 rounded-2xl outline-none transition-all text-sm font-medium"
                    />
                    <button
                      onClick={handleSearch}
                      disabled={state.isSearching}
                      className="absolute right-2 top-2 w-10 h-10 bg-indigo-600 text-white rounded-xl hover:bg-indigo-500 disabled:bg-slate-800 transition-all flex items-center justify-center shadow-lg shadow-indigo-900/40"
                    >
                      {state.isSearching ? (
                        <i className="fas fa-circle-notch fa-spin"></i>
                      ) : (
                        <i className="fas fa-bolt"></i>
                      )}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <ICPForm
              icp={state.icp}
              onChange={(icp) => setState((prev) => ({ ...prev, icp }))}
            />

            {state.leads.length > 0 && (
              <div className="glass-panel p-8 rounded-3xl h-64 border-indigo-500/20">
                <h3 className="text-[10px] font-black text-slate-500 mb-6 uppercase tracking-[0.2em]">
                  Batch Intelligence
                </h3>
                <ResponsiveContainer width="100%" height="80%">
                  <BarChart data={statsData}>
                    <XAxis
                      dataKey="name"
                      stroke="#475569"
                      fontSize={10}
                      axisLine={false}
                      tickLine={false}
                    />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#0f172a",
                        border: "1px solid rgba(255,255,255,0.1)",
                        borderRadius: "12px",
                        fontSize: "10px",
                      }}
                      itemStyle={{ color: "#fff" }}
                    />
                    <Bar dataKey="count" radius={[6, 6, 0, 0]}>
                      {statsData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.color}
                          fillOpacity={0.8}
                        />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            )}
          </div>

          {/* Right Panel: Data Stream */}
          <div className="lg:col-span-8">
            <div className="flex items-center justify-between mb-8">
              <div>
                <h2 className="text-3xl font-black text-white tracking-tight">
                  Intelligence Stream
                </h2>
                {state.leads.length > 0 && (
                  <p className="text-indigo-400 text-xs font-bold mt-1 uppercase tracking-widest">
                    {state.leads.length} Entities Identified
                  </p>
                )}
              </div>
              <div className="flex gap-3">
                <button className="glass-panel text-xs font-bold text-slate-300 px-4 py-2 rounded-xl hover:text-white transition-all flex items-center gap-2 border-white/5">
                  <i className="fas fa-layer-group"></i> Filter
                </button>
                <button className="bg-white/5 text-white text-xs font-bold px-4 py-2 rounded-xl hover:bg-white/10 transition-all flex items-center gap-2 border border-white/10">
                  <i className="fas fa-file-export"></i> Export
                </button>
              </div>
            </div>

            {state.isSearching ? (
              <div className="glass-panel rounded-[2rem] p-20 flex flex-col items-center justify-center text-center border-indigo-500/30">
                <div className="relative mb-10">
                  <div className="absolute inset-0 bg-indigo-500/20 blur-3xl animate-pulse"></div>
                  <div className="w-24 h-24 glass-panel text-indigo-400 rounded-3xl flex items-center justify-center border-indigo-500/50 relative z-10">
                    <i className="fas fa-satellite-dish text-4xl animate-pulse"></i>
                  </div>
                </div>
                <h3 className="text-2xl font-black text-white mb-4 tracking-tight">
                  Syncing Real-time Web Intelligence
                </h3>
                <p className="text-slate-400 max-w-sm font-medium leading-relaxed">
                  Our neural agents are currently traversing business signals
                  and news cycles to isolate high-value targets.
                </p>
                <div className="mt-12 w-80 bg-slate-900 rounded-full h-1.5 overflow-hidden border border-white/5">
                  <div className="bg-gradient-to-r from-indigo-600 via-purple-500 to-indigo-600 h-full w-full animate-[loading_1.5s_infinite] shadow-[0_0_15px_rgba(99,102,241,0.8)]"></div>
                </div>
                <style>{`
                  @keyframes loading {
                    0% { transform: translateX(-100%); }
                    100% { transform: translateX(100%); }
                  }
                `}</style>
              </div>
            ) : state.leads.length > 0 ? (
              <div className="space-y-6">
                {state.leads.map((lead) => (
                  <LeadCard
                    key={lead.id}
                    lead={lead}
                    onStatusChange={handleStatusChange}
                  />
                ))}
              </div>
            ) : error ? (
              <div className="glass-panel border-red-500/20 rounded-[2rem] p-16 text-center">
                <div className="text-red-500/80 text-5xl mb-6">
                  <i className="fas fa-shield-virus"></i>
                </div>
                <h3 className="text-xl font-black text-white mb-3 uppercase tracking-wider">
                  Interface Failure
                </h3>
                <p className="text-red-400/80 mb-8 font-medium">{error}</p>
                <button
                  onClick={handleSearch}
                  className="bg-red-500/20 text-red-400 px-8 py-3 rounded-2xl font-black hover:bg-red-500/30 transition-all border border-red-500/30 uppercase tracking-widest text-xs"
                >
                  Reset Link
                </button>
              </div>
            ) : (
              <div className="glass-panel border-dashed border-white/5 rounded-[2rem] p-24 flex flex-col items-center justify-center text-center opacity-80">
                <div className="text-7xl text-slate-800 mb-8">
                  <i className="fas fa-brain"></i>
                </div>
                <h3 className="text-2xl font-black text-slate-400 mb-3 tracking-tight">
                  Awaiting Target Parameters
                </h3>
                <p className="text-slate-600 max-w-sm font-medium">
                  Initialize search query and refine your ICP matrix to begin
                  the autonomous lead discovery process.
                </p>
              </div>
            )}
          </div>
        </div>
      </main>

      {/* Premium Floating Actions */}
      <div className="fixed bottom-8 right-8 flex flex-col gap-4">
        <button
          className="w-16 h-16 bg-gradient-to-br from-indigo-600 to-purple-600 text-white rounded-[20px] shadow-[0_10px_30px_rgba(99,102,241,0.4)] flex items-center justify-center hover:scale-105 active:scale-95 transition-all group relative border border-white/20"
          onClick={() => alert("Deployment mode coming soon.")}
        >
          <i className="fas fa-plus text-2xl"></i>
          <span className="absolute right-full mr-5 bg-indigo-900/90 backdrop-blur-md text-white text-[10px] font-black py-2 px-4 rounded-xl opacity-0 group-hover:opacity-100 transition-all whitespace-nowrap border border-white/10 uppercase tracking-[0.2em] translate-x-4 group-hover:translate-x-0">
            Deploy Unit
          </span>
        </button>
        <button
          className="w-16 h-16 glass-panel text-slate-400 rounded-[20px] flex items-center justify-center hover:text-white transition-all hover:scale-105 group relative"
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
        >
          <i className="fas fa-chevron-up"></i>
        </button>
      </div>
    </div>
  );
};

export default App;
