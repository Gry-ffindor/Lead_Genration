import React from "react";
import { Lead } from "../types";

interface LeadCardProps {
  lead: Lead;
  onStatusChange: (id: string, status: "shortlisted" | "rejected") => void;
}

const LeadCard: React.FC<LeadCardProps> = ({ lead, onStatusChange }) => {
  const isShortlisted = lead.status === "shortlisted";

  return (
    <div
      className={`glass-panel p-6 rounded-[1.5rem] border ${
        isShortlisted
          ? "border-indigo-500 shadow-[0_0_20px_rgba(99,102,241,0.15)] bg-indigo-500/5"
          : "border-white/5"
      } transition-all hover:border-white/10 group`}
    >
      <div className="flex justify-between items-start mb-5">
        <div className="flex gap-4">
          <div
            className={`w-12 h-12 rounded-2xl flex items-center justify-center font-black text-xl border transition-all ${
              isShortlisted
                ? "bg-indigo-500 text-white border-indigo-400"
                : "bg-white/5 text-indigo-400 border-white/5"
            }`}
          >
            {lead.name.charAt(0)}
          </div>
          <div>
            <h3 className="text-lg font-black text-white leading-tight group-hover:text-indigo-300 transition-colors">
              {lead.name}
            </h3>
            <a
              href={lead.website}
              target="_blank"
              rel="noopener noreferrer"
              className="text-slate-500 text-xs font-bold hover:text-indigo-400 flex items-center gap-1.5 transition-all mt-1 uppercase tracking-widest"
            >
              {lead.website.replace(/^https?:\/\/(www\.)?/, "")}{" "}
              <i className="fas fa-external-link-alt text-[8px]"></i>
            </a>
          </div>
        </div>
        <div className="flex gap-2">
          {lead.status === "new" && (
            <>
              <button
                onClick={() => onStatusChange(lead.id, "shortlisted")}
                className="w-10 h-10 flex items-center justify-center text-slate-500 hover:text-indigo-400 hover:bg-white/5 rounded-xl transition-all"
                title="Elite Selection"
              >
                <i className="fas fa-diamond text-lg"></i>
              </button>
              <button
                onClick={() => onStatusChange(lead.id, "rejected")}
                className="w-10 h-10 flex items-center justify-center text-slate-500 hover:text-rose-400 hover:bg-white/5 rounded-xl transition-all"
                title="Discard Entity"
              >
                <i className="fas fa-trash-alt text-lg"></i>
              </button>
            </>
          )}
          {isShortlisted && (
            <span className="bg-indigo-500 text-white px-4 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest flex items-center gap-2 shadow-[0_0_10px_rgba(99,102,241,0.5)]">
              <i className="fas fa-star"></i> Elite
            </span>
          )}
        </div>
      </div>

      <div className="mb-6">
        <h4 className="text-[10px] font-black text-slate-500 uppercase tracking-[0.2em] mb-3">
          AI Intelligence Report
        </h4>
        <p className="text-sm text-slate-400 leading-relaxed font-medium">
          {lead.summary}
        </p>
      </div>

      <div className="mb-6 bg-black/40 p-5 rounded-2xl border border-white/5 relative group/pitch">
        <div className="absolute top-3 right-3 opacity-0 group-hover/pitch:opacity-100 transition-opacity">
          <button className="text-slate-500 hover:text-white text-xs">
            <i className="fas fa-copy"></i>
          </button>
        </div>
        <h4 className="text-[10px] font-black text-indigo-400/70 uppercase tracking-[0.2em] mb-3 flex items-center gap-2">
          <i className="fas fa-bolt text-[10px]"></i> Strategic Opening
        </h4>
        <p className="text-sm text-slate-300 italic font-medium leading-relaxed">
          "{lead.pitch}"
        </p>
      </div>

      <div className="flex flex-wrap gap-2 mt-2">
        {lead.sources.map((source, i) => (
          <a
            key={i}
            href={source.uri}
            target="_blank"
            rel="noopener noreferrer"
            className="text-[9px] font-black uppercase tracking-widest bg-white/5 text-slate-500 px-3 py-1.5 rounded-lg border border-white/5 hover:bg-white/10 hover:text-slate-300 transition-all"
          >
            {source.title.substring(0, 25)}
          </a>
        ))}
        {lead.email && lead.email !== "Not found" && (
          <a
            href={`mailto:${lead.email}`}
            className="text-[9px] font-black uppercase tracking-widest bg-indigo-500/10 text-indigo-400 px-3 py-1.5 rounded-lg border border-indigo-500/20 hover:bg-indigo-500/20 hover:text-indigo-300 transition-all flex items-center gap-2"
          >
            <i className="fas fa-envelope"></i>
            {lead.email}
          </a>
        )}
      </div>
    </div>
  );
};

export default LeadCard;
