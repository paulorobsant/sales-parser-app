import "./styles.css";
import { FaFile } from "react-icons/fa";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

const FileInput = ({
  onChange = () => {},
  accept = "image/*",
  filename = "No file selected",
  error = true,
}) => {
  return (
    <label
      data-testid="fileinput-label"
      htmlFor="file-input"
      className={classNames("drop-container", error && "error")}
    >
      <FaFile size={50} />
      <span className="drop-title">Choose File</span>
      {filename}
      <input
        data-testid="fileinput-component"
        onChange={(e) => onChange(e)}
        type="file"
        id="file-input"
        accept={accept}
        required
      />
    </label>
  );
};

export default FileInput;
