# Robotic Process Automation for Structured Health Data in Romanian Clinics

### Project Overview

This project demonstrates a complete automation pipeline for processing Romanian day hospitalization forms, many of which contain handwritten content and unstructured fields. Using UiPath's Document Understanding framework, combined with OCR engines, a custom taxonomy, HL7 FHIR mapping, and REST API integration, the solution enables scalable, standards-compliant digitization of semi-structured medical documents.

The system is modular and supports batch processing, validation via UiPath Validation Station, and export to multiple targets including Excel, a public FHIR server (HAPI FHIR), and a custom FastAPI endpoint.

---

## Features

-  **Document Understanding (OCR + Taxonomy)**  
  Extracts structured data from scanned PDFs, including handwritten and printed content.

-  **Optional Generative AI Integration**  
  Enhances data extraction through semantic understanding (only in alternative pipeline).

-  **Validation Station Support**  
  Human-in-the-loop mechanism for correcting low-confidence extractions.

-  **Export to HL7 FHIR**  
  Generates Patient, Condition, and Procedure resources and sends them to a FHIR server.

-  **FastAPI Endpoint Integration**  
  Simulates custom health information integration using RESTful APIs.

-  **Excel Logging**  
  Each processed case is logged to an Excel file for auditing and statistical analysis.

-  **Batch Processing Loop**  
  Supports processing of multiple documents in a single unattended run.

---

## System Requirements

| Component             | Specification                        |
|----------------------|--------------------------------------|
| Operating System      | Windows 10 64-bit                    |
| UiPath Version        | Studio 2024.2 Community Edition      |
| OCR Engine Used       | UiPath Document OCR (ML)             |
| .NET Runtime          | .NET 6.0 (for ML Packages)           |
| Python                | minimum version 3.10                 |

---

## Running the Project

1. Open and start the API 
2. Open the Document Understanding solution in UiPath Studio 2024.2+
3. Open the Document Understanding workflow (`document_understanding.xaml`)
5. Change the path to the director where your PDFs are saved
6. Run the Document Understanding workflow (`document_understanding.xaml`) to start the batch automation
7. Review and validate data using Validation Station
8. Open the AI pipeline and run the main workflow to use AI extraction (optional)
9. The extracted data will be:
   - Logged in Excel
   - Sent to the HAPI FHIR server
   - Sent to the FastAPI server
     

---

## Notes

- The solution achieves **TRL 4**, having been tested with real documents in a lab setup.
- Designed for adaptability, it can be expanded to process other types of forms or be integrated into national EHR systems.
- For better performance, enterprise UiPath components like AI Center and Orchestrator can be integrated.
