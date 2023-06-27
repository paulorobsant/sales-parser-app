import "./styles.css";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

const Button = ({
  label = "Save",
  variant = "contained",
  fullWidth = true,
  onClick = () => {},
  disabled = false,
  type = "button",
}) => {
  return (
    <button
      data-testid="button-component"
      className={classNames(
        "button-component",
        variant,
        disabled && "disabled",
        fullWidth && "fullWidth"
      )}
      onClick={() => {
        !disabled && onClick();
      }}
      type={type}
    >
      {label}
    </button>
  );
};
export default Button;
