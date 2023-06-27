import { render, screen } from "@testing-library/react";
import AlertNotification from ".";
import userEvent from "@testing-library/user-event";

describe("AlertNotification", () => {
  it("should render component ==> AlertNotification", () => {
    render(<AlertNotification isOpen={true} />);

    expect(screen.getByTestId("alert-component")).toBeInTheDocument();
  });

  it("should not render component ==> AlertNotification", () => {
    render(<AlertNotification isOpen={false} />);

    expect(screen.queryByTestId("alert-component")).not.toBeInTheDocument();
  });

  it("should render title and message passed prop to component ==> AlertNotification", () => {
    render(
      <AlertNotification
        isOpen={true}
        title={"Novo Titulo"}
        message="Nova mensagem"
      />
    );

    expect(screen.getByText("Novo Titulo")).toBeInTheDocument();
    expect(screen.getByText("Nova mensagem")).toBeInTheDocument();
  });

  it("should render error alert ==> AlertNotification", () => {
    render(<AlertNotification isOpen={true} type="error" />);

    expect(screen.getByTestId("error-icon")).toBeInTheDocument();
  });

  it("should render success alert ==> AlertNotification", () => {
    render(<AlertNotification isOpen={true} type="success" />);

    expect(screen.getByTestId("success-icon")).toBeInTheDocument();
  });

  it("should render info alert ==> AlertNotification", () => {
    render(<AlertNotification isOpen={true} type="info" />);

    expect(screen.getByTestId("info-icon")).toBeInTheDocument();
  });

  it("should render warning alert ==> AlertNotification", () => {
    render(<AlertNotification isOpen={true} type="warning" />);

    expect(screen.getByTestId("warning-icon")).toBeInTheDocument();
  });

  it("should call event button click ==> AlertNotification", () => {
    const mockOnclickEvent = jest.fn();

    render(
      <AlertNotification
        isOpen={true}
        type="warning"
        closeNotification={mockOnclickEvent}
      />
    );

    const button = screen.getByTestId("icon-button");

    userEvent.click(button);

    expect(mockOnclickEvent).toHaveBeenCalled();
  });
});
