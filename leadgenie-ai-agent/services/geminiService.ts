import { ICP, Lead } from "../types";

export const searchLeads = async (query: string, icp: ICP): Promise<Lead[]> => {
  try {
    const response = await fetch("http://localhost:8000/api/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query,
        icp,
        max_results: 5, // Default for now
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`API Error: ${response.status} - ${errorText}`);
    }

    const leads: Lead[] = await response.json();
    return leads;
  } catch (error) {
    console.error("Backend Search Error:", error);
    throw error;
  }
};
