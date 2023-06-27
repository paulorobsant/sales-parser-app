import "./styles.css";

function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}

const CircularButton = ({
  label = "Save",
  variant = "contained",
  onClick = () => {},
  disabled = false,
}) => {
  return (
    <button
      data-testid="circularbutton-component"
      className={classNames(
        "circularbutton-component",
        variant,
        disabled && "disabled"
      )}
      onClick={() => {
        !disabled && onClick();
      }}
    >
      {label}
    </button>
  );
};
export default CircularButton;
