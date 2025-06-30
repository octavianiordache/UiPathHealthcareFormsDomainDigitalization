# Automating Romanian Medical Discharge Forms Using RPA and HL7 FHIR

### Project Overview

This project demonstrates a complete automation pipeline for processing Romanian day hospitalization forms, many of which contain handwritten content and unstructured fields. Using UiPath's Document Understanding framework, combined with OCR engines, a custom taxonomy, HL7 FHIR mapping, and REST API integration, the solution enables scalable, standards-compliant digitization of semi-structured medical documents.

The system is modular and supports batch processing, validation via UiPath Validation Station, and export to multiple targets including Excel, a public FHIR server (HAPI FHIR), and a custom FastAPI endpoint.

---

## Features

- 🧾 **Document Understanding (OCR + Taxonomy)**  
  Extracts structured data from scanned PDFs, including handwritten and printed content.

- 🧠 **Optional Generative AI Integration**  
  Enhances data extraction through semantic understanding (only in alternative pipeline).

- ✅ **Validation Station Support**  
  Human-in-the-loop mechanism for correcting low-confidence extractions.

- 📤 **Export to HL7 FHIR**  
  Generates Patient, Condition, and Procedure resources and sends them to a FHIR server.

- 🗂️ **FastAPI Endpoint Integration**  
  Simulates custom health information integration using RESTful APIs.

- 📊 **Excel Logging**  
  Each processed case is logged to an Excel file for auditing and statistical analysis.

- 🔁 **Batch Processing Loop**  
  Supports processing of multiple documents in a single unattended run.

---

## System Requirements

| Component             | Specification                        |
|----------------------|--------------------------------------|
| Operating System      | Windows 11 Pro 64-bit                |
| Processor             | Intel Core i7-11800H @ 2.30GHz       |
| RAM                   | 16 GB DDR4                           |
| Disk                  | 512 GB NVMe SSD                      |
| UiPath Version        | Studio 2024.2 Community Edition      |
| OCR Engine Used       | UiPath Document OCR (ML)             |
| .NET Runtime          | .NET 6.0 (for ML Packages)           |

---

## Folder Structure

```
project-folder/
│
├── UiPath_Workflows/           # Main .xaml files
├── Taxonomy/                   # Custom DU taxonomy for field extraction
├── FastAPI_Server/             # Python API for custom resource ingestion
├── Sample_Documents/           # Example medical PDFs for testing
├── Outputs/                    # Excel exports and FHIR response logs
└── README.md
```

---

## Running the Project

1. Open the UiPath solution in UiPath Studio 2024.2+
2. Configure the OCR engine and taxonomy path inside the DU pipeline
3. Place your scanned PDFs in the `Sample_Documents` folder
4. Run the main workflow (`Main.xaml`) to start the batch automation
5. Review and validate data using Validation Station (if enabled)
6. The extracted data will be:
   - Logged in Excel
   - Sent to the HAPI FHIR server (if configured)
   - Sent to the FastAPI server (optional)

---

## Notes

- The solution achieves **TRL 4**, having been tested with real documents in a lab setup.
- Designed for adaptability, it can be expanded to process other types of forms or be integrated into national EHR systems.
- For better performance, enterprise UiPath components like AI Center and Orchestrator can be integrated.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more information.