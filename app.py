import React, { useState } from "react";
import axios from "axios";

const JobRecommendation = () => {
  const [skills, setSkills] = useState("");
  const [experience, setExperience] = useState("");
  const [cgpa, setCgpa] = useState("");
  const [jobs, setJobs] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.post("https://job-recommendation-api.onrender.com/recommend, {
        skills,
        experience: Number(experience),
        cgpa: Number(cgpa),
      });
      setJobs(response.data);
    } catch (error) {
      console.error("Error fetching jobs", error);
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Job Recommendation System</h1>
      <input
        className="border p-2 w-full mb-2"
        type="text"
        placeholder="Enter your skills"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />
      <input
        className="border p-2 w-full mb-2"
        type="number"
        placeholder="Years of experience"
        value={experience}
        onChange={(e) => setExperience(e.target.value)}
      />
      <input
        className="border p-2 w-full mb-2"
        type="number"
        placeholder="Enter CGPA"
        value={cgpa}
        onChange={(e) => setCgpa(e.target.value)}
      />
      <button className="bg-blue-500 text-white p-2 w-full" onClick={handleSearch}>
        Get Recommendations
      </button>
      <div className="mt-4">
        {jobs.length > 0 ? (
          <ul>
            {jobs.map((job, index) => (
              <li key={index} className="border p-2 mb-2">
                <h2 className="font-bold">{job.jobTitle}</h2>
                <p><strong>Skills:</strong> {job.skills}</p>
                <p><strong>Experience:</strong> {job.minExp} - {job.maxExp} years</p>
                <p><strong>Location:</strong> {job.location}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No recommendations found.</p>
        )}
      </div>
    </div>
  );
};

export default JobRecommendation;


# In[ ]:




