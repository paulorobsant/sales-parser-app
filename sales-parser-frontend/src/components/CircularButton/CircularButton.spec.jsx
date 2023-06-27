import { render, screen } from "@testing-library/react";
import CircularButton from ".";
import userEvent from "@testing-library/user-event";

describe("CircularButton", () => {
  it("should render component ==> CircularButton", () => {
    render(<CircularButton />);

    expect(screen.getByTestId("circularbutton-component")).toBeInTheDocument();
  });

  it("should render prop passed label to component ==> CircularButton", () => {
    render(<CircularButton label="Nova label" />);

    expect(screen.getByText("Nova label")).toBeInTheDocument();
  });

  it("should call on click event ==> CircularButton", () => {
    const mockOnclickEvent = jest.fn();

    render(<CircularButton onClick={mockOnclickEvent} />);

    const button = screen.getByTestId("circularbutton-component");

    userEvent.click(button);

    expect(mockOnclickEvent).toHaveBeenCalled();
  });

  it("should try to click when is disabled ==> CircularButton", () => {
    const mockOnclickEvent = jest.fn();

    render(<CircularButton onClick={mockOnclickEvent} disabled />);

    const button = screen.getByTestId("circularbutton-component");

    userEvent.click(button);

    expect(mockOnclickEvent).not.toHaveBeenCalled();
  });
});
