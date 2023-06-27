import { render, screen } from "@testing-library/react";
import FileInput from ".";
import userEvent from "@testing-library/user-event";

describe("FileInput", () => {
  it("should render component ==> FileInput", () => {
    render(<FileInput />);

    expect(screen.getByTestId("fileinput-component")).toBeInTheDocument();
  });

  it("should render filename passed by prop to component ==> FileInput", () => {
    render(<FileInput filename="Novo arquivo" />);

    expect(screen.getByText("Novo arquivo")).toBeInTheDocument();
  });

  it("should upload a file ==> FileInput", () => {
    const mockOnChange = jest.fn();
    const file = new File(["hello"], "hello.txt", { type: "txt" });

    render(<FileInput onChange={mockOnChange} />);

    const input = screen.getByTestId("fileinput-component");

    userEvent.upload(input, file);

    //Checking how many times the event is called
    expect(mockOnChange).toHaveBeenCalledTimes(1);

    //Checking number of files present in the array
    expect(input.files).toHaveLength(1);

    //Checking if the file that was passed is the same
    expect(input.files[0]).toStrictEqual(file);

    //Checking file name
    expect(input.files[0].name).toBe("hello.txt");

    //Checking file types
    expect(input.files[0].type).toBe("txt");
  });

  it("should render error class passed by prop to component ==> FileInput", () => {
    render(<FileInput error={true} />);

    const container = screen.getByTestId("fileinput-label");

    expect(container).toHaveClass("error");
  });

  it("should not render error class passed by prop to component ==> FileInput", () => {
    render(<FileInput error={false} />);

    const container = screen.getByTestId("fileinput-label");

    expect(container).not.toHaveClass("error");
  });
});
