# Individual Reflection

## Technical Contributions

### Data Processing Notebook  
One of my primary responsibilities in our project was developing the data processing pipeline, which involved integrating and cleaning data from multiple sources. The key aspects of my contribution included:

#### Processing Odds Data  
I designed the `process_odds_data` function to extract relevant match and odds data from the raw JSON files provided by the Odds API. This function ensured:  
- Duplicate entries were avoided using a unique match ID system.  
- Only relevant head-to-head odds were processed.  
- Odds from various bookmakers were standardized and structured properly.  

#### Batch Processing of JSON Files  
Since our dataset consisted of multiple JSON files, I developed `process_all_files`, a function that iteratively loaded, processed, and combined data from all JSON files in our dataset directory. This automation was crucial in maintaining consistency and efficiency.  

#### Match Outcomes Data Processing  
I also developed the `load_and_concatenate_premier_league_data` function, which extracted specific columns from multiple CSV files containing historical match results. This allowed us to align match results with the processed odds data seamlessly.  

#### Fixture ID Generation  
To ensure a reliable way to match data between different sources, I implemented `generate_fixture_id_api`, which generated unique fixture IDs based on team names and match dates. This step was critical for merging datasets accurately.  

## Formatting and Documentation  

Another significant contribution I made to the project was writing and structuring the project's documentation, including:  

- **`README.md`**: I wrote the README file to provide an overview of the project, including setup instructions, data sources, methodology, and how to navigate our repository. The README ensured clarity for new users and future contributors.  
- **`index.md`**: I created the index documentation for our project, summarizing our research areas, methodologies, and findings in a structured manner. This helped in making our work easily accessible and digestible.  

## Team Collaboration  

### Role in Team Coordination  
Throughout the project, I actively collaborated with team members to ensure smooth data integration. Given that my work served as the foundation for subsequent backtesting and analysis, I:  

- Regularly updated the team on data processing progress, ensuring that their models and strategies had clean and structured data.  
- Participated in discussions to align data formats with analysis requirements.  
- Provided insights on data integrity, helping refine assumptions for betting strategies.  

### Supporting Team Members  
Beyond my primary responsibilities, I also assisted teammates by:  

- **Debugging and Code Reviews**: I reviewed and debugged scripts, particularly in the backtesting notebooks, ensuring data consistency and alignment with our processed dataset.  
- **Ensuring Documentation Clarity**: I worked closely with team members to ensure that the README and index documentation accurately reflected everyone’s contributions and project methodology.  

### Conflict Resolution  
While we had a strong collaborative effort, there were occasional disagreements, particularly regarding how fixture IDs should be structured for merging datasets. Some team members initially preferred different formatting methods. To resolve this, I:  

- Proposed test cases comparing different approaches.  
- Demonstrated why my chosen approach minimized errors and inconsistencies.  
- Compromised by integrating additional validation checks to accommodate edge cases.  

## Learning Journey  

### Skills Developed  
This project significantly enhanced my technical and collaborative skills:  

- **Data Processing & Cleaning**: I deepened my understanding of handling real-world datasets, particularly in sports analytics.  
- **SQL & Pandas Proficiency**: Working with structured and unstructured data improved my ability to manipulate large datasets efficiently.  
- **Markdown & Documentation**: Writing clear and structured documentation improved my ability to communicate technical concepts effectively.  
- **Collaboration & Code Integration**: I gained experience in working with a team on a shared codebase, handling dependencies, and ensuring code readability.  

### Challenges Overcome  
The biggest challenges I faced were:  

- **Handling Inconsistent Data Formats**: The data from different sources used varying team name formats. I resolved this by creating robust mapping dictionaries that standardized names.  
- **Ensuring Scalable Data Processing**: Given the large dataset, initial processing attempts were slow. By implementing batch processing and optimizing SQL storage, I significantly reduced runtime.  
- **Balancing Workload**: With documentation responsibilities in addition to coding, I managed my time effectively by setting clear milestones and prioritizing tasks.  

### Areas for Future Growth  
While I gained valuable experience, I recognize areas where I can further improve:  

- **Advanced SQL & Database Management**: Optimizing queries and database structures would further improve data handling efficiency.  
- **Machine Learning for Predictive Analysis**: Applying ML models to betting data could be a future extension of this research.  
