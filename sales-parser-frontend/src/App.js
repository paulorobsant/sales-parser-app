import { useEffect, useState } from "react";
import "./App.css";
import Button from "./components/Button";
import FileInput from "./components/FileInput";
import AlertNotification from "./components/AlertNotification";

function App() {
  const [formData, setFormData] = useState({
    file: "",
  });

  const [formError, setFormError] = useState({
    file: false,
  });

  const [alertNotiticationInformation, setAlertNotiticationInformation] =
    useState({
      isOpen: false,
      type: "info",
      title: "Title",
      message: "Lorem ipsum dolum",
    });

  const sendFile = async () => {
    var form = new FormData();

    form.append("files", formData.file, formData.file.name);

    await fetch(process.env.REACT_APP_API_URL + "/upload_file/", {
      method: "POST",
      body: form,
    })
      .then(async (response) => {
        const result = await response.json();

        if (response.status === 201) {
          setAlertNotiticationInformation({
            ...alertNotiticationInformation,
            isOpen: true,
            type: "success",
            title: "File sent successfully!",
            message: result.detail,
          });
        } else {
          setAlertNotiticationInformation({
            ...alertNotiticationInformation,
            isOpen: true,
            type: "error",
            title: "Error when uploading the file!",
            message: "Error: " + result.detail,
          });
        }
      })
      .catch((error) => {
        setAlertNotiticationInformation({
          ...alertNotiticationInformation,
          isOpen: true,
          type: "error",
          title: "Error when uploading the file!",
          message: "Error: " + error,
        });
      });
  };

  const handleOnSubmit = () => {
    if (formData.file) {
      sendFile();
    } else {
      setFormError({
        ...formError,
        file: true,
      });

      setAlertNotiticationInformation({
        ...alertNotiticationInformation,
        isOpen: true,
        type: "error",
        title: "Adding a file is mandatory!",
        message: "Add a .txt file regarding sales.",
      });
    }
  };

  useEffect(() => {
    if (formError.file) {
      setFormError({
        file: false,
      });
    }
  }, [formData]);

  useEffect(() => {
    const keyDownHandler = (event) => {
      if (event.key === "Enter" && formData.file) {
        event.preventDefault();

        handleOnSubmit();
      }
    };

    document.addEventListener("keydown", keyDownHandler);

    return () => {
      document.removeEventListener("keydown", keyDownHandler);
    };
  }, []);

  return (
    <div className="App">
      <div className="container">
        <h1 className="title">Select the sales file</h1>
        <FileInput
          error={formError.file}
          accept=".txt"
          filename={formData?.file?.name}
          onChange={(e) =>
            setFormData({ ...formData, file: e.target.files[0] })
          }
        />
        <div className="button-container">
          <Button
            disabled={!formData.file}
            onClick={() => handleOnSubmit()}
            type="submit"
          />
        </div>

        <AlertNotification
          type={alertNotiticationInformation.type}
          isOpen={alertNotiticationInformation.isOpen}
          title={alertNotiticationInformation.title}
          message={alertNotiticationInformation.message}
          closeNotification={() =>
            setAlertNotiticationInformation({
              ...alertNotiticationInformation,
              isOpen: false,
            })
          }
        />
      </div>
    </div>
  );
}

export default App;
