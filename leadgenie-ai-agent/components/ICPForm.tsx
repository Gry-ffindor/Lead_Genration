
import React from 'react';
import { ICP } from '../types';

interface ICPFormProps {
  icp: ICP;
  onChange: (icp: ICP) => void;
}

const ICPForm: React.FC<ICPFormProps> = ({ icp, onChange }) => {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    onChange({ ...icp, [name]: value });
  };

  return (
    <div className="glass-panel p-8 rounded-3xl relative overflow-hidden">
      <div className="absolute top-0 left-0 w-32 h-32 bg-purple-600/5 blur-3xl -ml-16 -mt-16"></div>
      <div className="flex items-center gap-3 mb-8">
        <div className="w-8 h-8 rounded-lg bg-indigo-500/10 flex items-center justify-center">
            <i className="fas fa-sliders-h text-indigo-400 text-sm"></i>
        </div>
        <h2 className="text-white font-bold tracking-tight">Ideal Customer Matrix</h2>
      </div>
      <div className="grid grid-cols-1 gap-5">
        <div className="grid grid-cols-2 gap-4">
            <div>
            <label className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2">Industry</label>
            <input
                type="text"
                name="industry"
                value={icp.industry}
                onChange={handleChange}
                placeholder="Vertical"
                className="glass-input w-full px-4 py-3 rounded-xl text-sm outline-none transition-all"
            />
            </div>
            <div>
            <label className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2">Firm Size</label>
            <input
                type="text"
                name="companySize"
                value={icp.companySize}
                onChange={handleChange}
                placeholder="Headcount"
                className="glass-input w-full px-4 py-3 rounded-xl text-sm outline-none transition-all"
            />
            </div>
        </div>
        
        <div>
          <label className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2">Territory</label>
          <input
            type="text"
            name="targetRegion"
            value={icp.targetRegion}
            onChange={handleChange}
            placeholder="Geographic Focus"
            className="glass-input w-full px-4 py-3 rounded-xl text-sm outline-none transition-all"
          />
        </div>
        
        <div>
          <label className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2">Tech Stack</label>
          <input
            type="text"
            name="technologies"
            value={icp.technologies}
            onChange={handleChange}
            placeholder="Signals (e.g. AWS)"
            className="glass-input w-full px-4 py-3 rounded-xl text-sm outline-none transition-all"
          />
        </div>

        <div>
          <label className="block text-[10px] font-black text-slate-500 uppercase tracking-widest mb-2">Pain Point Vectors</label>
          <textarea
            name="painPoints"
            value={icp.painPoints}
            onChange={handleChange}
            placeholder="What friction do they face?"
            className="glass-input w-full px-4 py-3 rounded-xl text-sm outline-none transition-all h-24 resize-none"
          />
        </div>
      </div>
    </div>
  );
};

export default ICPForm;
