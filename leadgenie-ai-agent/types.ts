export interface ICP {
  industry: string;
  companySize: string;
  targetRegion: string;
  painPoints: string;
  technologies: string;
}

export interface Lead {
  id: string;
  name: string;
  website: string;
  industry: string;
  size: string;
  summary: string;
  email: string;
  pitch: string;
  sources: { title: string; uri: string }[];
  status: "new" | "shortlisted" | "rejected";
}

export interface ResearchResult {
  leads: Lead[];
}

export interface AppState {
  icp: ICP;
  leads: Lead[];
  isSearching: boolean;
  searchQuery: string;
}
