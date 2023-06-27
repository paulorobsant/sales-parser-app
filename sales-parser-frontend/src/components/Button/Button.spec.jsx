import { render, screen } from "@testing-library/react";
import Button from ".";
import userEvent from "@testing-library/user-event";

describe("Button", () => {
  it("should render component ==> Button", () => {
    render(<Button />);

    expect(screen.getByTestId("button-component")).toBeInTheDocument();
  });

  it("should render prop passed label to component ==> Button", () => {
    render(<Button label="Nova label" />);

    expect(screen.getByText("Nova label")).toBeInTheDocument();
  });

  it("should call on click event ==> Button", () => {
    const mockOnclickEvent = jest.fn();

    render(<Button onClick={mockOnclickEvent} />);

    const button = screen.getByTestId("button-component");

    userEvent.click(button);

    expect(mockOnclickEvent).toHaveBeenCalled();
  });

  it("should try to click when is disabled ==> Button", () => {
    const mockOnclickEvent = jest.fn();

    render(<Button onClick={mockOnclickEvent} disabled />);

    const button = screen.getByTestId("button-component");

    userEvent.click(button);

    expect(mockOnclickEvent).not.toHaveBeenCalled();
  });
});
