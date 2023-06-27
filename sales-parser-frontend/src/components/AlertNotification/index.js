import {
  FaRegTimesCircle,
  FaCheckCircle,
  FaExclamationTriangle,
  FaExclamationCircle,
} from "react-icons/fa";
import "./styles.css";
import { useEffect, useState } from "react";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

const AlertNotification = ({
  title = "Titulo",
  message = "Lorem ipsum dolum",
  type = "success",
  isOpen = false,
  closeNotification = () => {},
}) => {
  const [timeoutClose, setTimeoutClose] = useState(false);

  useEffect(() => {
    if (isOpen) {
      setTimeoutClose(
        setTimeout(() => {
          closeNotification();
        }, 5000)
      );
    } else {
      clearTimeout(timeoutClose);
    }
  }, [isOpen]);

  return (
    <>
      {isOpen && (
        <div
          data-testid="alert-component"
          className={classNames(
            "alert-container",
            type,
            isOpen ? "active" : "inactive"
          )}
        >
          <div className={classNames("icon-container", type)}>
            {type === "success" && (
              <FaCheckCircle data-testid="success-icon" size={30} />
            )}

            {type === "error" && (
              <FaRegTimesCircle data-testid="error-icon" size={30} />
            )}

            {(type === "info" || type.length === 0) && (
              <FaExclamationCircle data-testid="info-icon" size={30} />
            )}

            {type === "warning" && (
              <FaExclamationTriangle data-testid="warning-icon" size={30} />
            )}
          </div>

          <div className="text-container">
            {title && <p className="title">{title}</p>}
            {message && <p className="message">{message}</p>}
          </div>

          <div className="close-container">
            <button
              data-testid="icon-button"
              className="icon-button"
              onClick={closeNotification}
            >
              <FaRegTimesCircle size={20} />
            </button>
          </div>
        </div>
      )}
    </>
  );
};
export default AlertNotification;
