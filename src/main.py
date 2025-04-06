import random
import pygame
import ctypes

pygame.init()
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

def setWindowTransparency(hwnd, opacity=255):
    user32 = ctypes.windll.user32
    user32.SetWindowLongA(hwnd, GWL_EXSTYLE, 
                         user32.GetWindowLongA(hwnd, GWL_EXSTYLE) | WS_EX_LAYERED)
    user32.SetLayeredWindowAttributes(hwnd, 0, opacity, LWA_ALPHA)

def minimizeWindow(hwnd):
    user32 = ctypes.windll.user32
    user32.ShowWindow(hwnd, 6)

def setWindowRoundedCorners(hwnd, radius=15):
    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long),
                   ("right", ctypes.c_long), ("bottom", ctypes.c_long)]

    rect = RECT()
    user32 = ctypes.windll.user32
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    region = ctypes.windll.gdi32.CreateRoundRectRgn(0, 0, width, height, radius, radius)
    result = user32.SetWindowRgn(hwnd, region, True)
    ctypes.windll.gdi32.DeleteObject(region)
    return result

def pickBeginningState():
    userStates = ["x", "o"]
    beginningState = random.choice(userStates)
    return beginningState

def switchPlayer(turn):
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
    return turn

class Cell:
    def __init__(self, x1, x2, y1, y2):
        self.full = False
        self.width = [x1, x2]
        self.height = [y1, y2]
        self.symbol = None

def getSelectedCell(mousePos, cells):
    for i, cell in enumerate(cells):
        if mousePos[0] in range(cell.width[0], cell.width[1]) and mousePos[1] in range(cell.height[0], cell.height[1]):
            row = i // 3
            col = i % 3
            return cell, row, col
    return None, None, None

def checkAvailability(cell, row, col, cellStates):
    if not cell.full and cellStates[row][col] == 0:
        return True
    else:
        return False

def markCell(cell, row, col, cellsStates, turn):
    cell.full = True
    cell.symbol = turn
    if turn == "x":
        cellsStates[row][col] = 1
    else:
        cellsStates[row][col] = 2
    return switchPlayer(turn), turn

def renderOnCell(window, cell, turn, color):
    centerOfCellX = (cell.width[0] + cell.width[1]) // 2
    centerOfCellY = (cell.height[0] + cell.height[1]) // 2
    if turn == "x":
        pygame.draw.circle(window, color, (centerOfCellX, centerOfCellY), 30, 4)
    else:
        pygame.draw.line(window, color, (centerOfCellX - 26, centerOfCellY - 26), (centerOfCellX + 26, centerOfCellY + 26), 6)
        pygame.draw.line(window, color, (centerOfCellX - 26, centerOfCellY + 26), (centerOfCellX + 26, centerOfCellY - 26), 6)

def drawGrid(window, color, vertRightX, vertRightY, vertLeftX, vertLeftY, horizRightX, horizRightY, horizLeftX, horizLeftY, edgeRightX, edgeRightY, edgeLeftX, edgeLeftY, edgeTopX, edgeTopY, edgeBottomX, edgeBottomY, horizontalWidth, horizontalHeight, verticalWidth, verticalHeight):
    pygame.draw.rect(window, color, (vertRightX, vertRightY, verticalWidth, verticalHeight))
    pygame.draw.rect(window, color, (vertLeftX, vertLeftY, verticalWidth, verticalHeight))
    pygame.draw.rect(window, color, (horizRightX, horizRightY, horizontalWidth, horizontalHeight))
    pygame.draw.rect(window, color, (horizLeftX, horizLeftY, horizontalWidth, horizontalHeight))
    pygame.draw.rect(window, color, (edgeRightX, edgeRightY, verticalWidth, verticalHeight))
    pygame.draw.rect(window, color, (edgeLeftX, edgeLeftY, verticalWidth, verticalHeight))
    pygame.draw.rect(window, color, (edgeTopX, edgeTopY, horizontalWidth, horizontalHeight))
    pygame.draw.rect(window, color, (edgeBottomX, edgeBottomY, horizontalWidth, horizontalHeight))

def drawExitRect(surface, color, rect, border_radius):
    x, y, width, height = rect

    pygame.draw.rect(surface, color, (x + border_radius, y, width - 2 * border_radius, height))
    pygame.draw.rect(surface, color, (x, y + border_radius, width, height - 2 * border_radius))
    pygame.draw.circle(surface, color, (x + border_radius, y + border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + width - border_radius, y + border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + border_radius, y + height - border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + width - border_radius, y + height - border_radius), border_radius)

def drawMinRect(surface, color, rect, border_radius):
    x, y, width, height = rect

    pygame.draw.rect(surface, color, (x + border_radius, y, width - 2 * border_radius, height))
    pygame.draw.rect(surface, color, (x, y + border_radius, width, height - 2 * border_radius))
    pygame.draw.circle(surface, color, (x + border_radius, y + border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + width - border_radius, y + border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + border_radius, y + height - border_radius), border_radius)
    pygame.draw.circle(surface, color, (x + width - border_radius, y + height - border_radius), border_radius)

def checkIfDraw(cells):
    for cell in cells:
        if not cell.full:
            return False
    return True

def checkRows(cellsStates):
    row1EqualX = cellsStates[0][0] == cellsStates[0][1] == cellsStates[0][2] == 1
    row2EqualX = cellsStates[1][0] == cellsStates[1][1] == cellsStates[1][2] == 1
    row3EqualX = cellsStates[2][0] == cellsStates[2][1] == cellsStates[2][2] == 1
    row1EqualO = cellsStates[0][0] == cellsStates[0][1] == cellsStates[0][2] == 2
    row2EqualO = cellsStates[1][0] == cellsStates[1][1] == cellsStates[1][2] == 2
    row3EqualO = cellsStates[2][0] == cellsStates[2][1] == cellsStates[2][2] == 2
    if row1EqualX or row2EqualX or row3EqualX:
        return 1
    elif row1EqualO or row2EqualO or row3EqualO:
        return 2
    else:
        return None

def checkCols(cellsStates):
    col1EqualX = cellsStates[0][0] == cellsStates[1][0] == cellsStates[2][0] == 1
    col2EqualX = cellsStates[0][1] == cellsStates[1][1] == cellsStates[2][1] == 1
    col3EqualX = cellsStates[0][2] == cellsStates[1][2] == cellsStates[2][2] == 1
    col1EqualO = cellsStates[0][0] == cellsStates[1][0] == cellsStates[2][0] == 2
    col2EqualO = cellsStates[0][1] == cellsStates[1][1] == cellsStates[2][1] == 2
    col3EqualO = cellsStates[0][2] == cellsStates[1][2] == cellsStates[2][2] == 2
    if col1EqualX or col2EqualX or col3EqualX:
        return 1
    elif col1EqualO or col2EqualO or col3EqualO:
        return 2
    else:
        return None

def checkDiags(cellsStates):
    diag1EqualX = cellsStates[0][0] == cellsStates[1][1] == cellsStates[2][2] == 1
    diag2EqualX = cellsStates[0][2] == cellsStates[1][1] == cellsStates[2][0] == 1
    diag1EqualO = cellsStates[0][0] == cellsStates[1][1] == cellsStates[2][2] == 2
    diag2EqualO = cellsStates[0][2] == cellsStates[1][1] == cellsStates[2][0] == 2
    if diag1EqualX or diag2EqualX:
        return 1
    elif diag1EqualO or diag2EqualO:
        return 2
    else:
        return None

def compareCells(cells, cellsStates):
    if checkIfDraw(cells) and checkRows(cellsStates) is None and checkCols(cellsStates) is None and checkDiags(cellsStates) is None:
        return 0
    else:
        if checkRows(cellsStates) is not None:
            return checkRows(cellsStates)
        if checkCols(cellsStates) is not None:
            return checkCols(cellsStates)
        if checkDiags(cellsStates) is not None:
            return checkDiags(cellsStates)
        else:
            return None

def displayResult(window, result, backgroundColor, font):
    if result == 0:
        text = font.render("Draw!", True, (255, 255, 255))
    elif result == 1:
        text = font.render("X Wins!", True, (255, 255, 255))
    elif result == 2:
        text = font.render("O Wins!", True, (255, 255, 255))
    else :
        text = font.render("This should never happen!", True, (255,255,255))
    textRect = text.get_rect(center=(200, 235))
    window.fill(backgroundColor)
    window.blit(text, textRect)
    pygame.display.update()
    pygame.time.wait(3000)

def askIfReplay(window, backgroundColor, font):
    while True:
        text = font.render("Do you want to replay?", True, (255, 255, 255))
        textRect = text.get_rect(center=(200, 120))
        window.fill(backgroundColor)
        window.blit(text, textRect)
        yesColor = (235, 215, 255)
        yesColorShadow = (205, 185, 225)
        noColor = (255,255,255)
        noColorShadow = (225,225,225)
        pygame.draw.rect(window, yesColorShadow,(80,240,100,50))
        pygame.draw.rect(window, yesColor,(77,237,100,50))
        pygame.draw.rect(window, noColorShadow,(220,240,100,50))
        pygame.draw.rect(window, noColor,(217,237,100,50))
        yesText = font.render("YES" , True, (34,34,34))
        noText = font.render("NO", True, (34,34,34))
        window.blit(yesText,(100,247,100,50))
        window.blit(noText,(250,247,100,50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = event.pos
                if (mousePos[0] in range(77, 177) and mousePos[1] in range(237, 287)):
                    return 1
                elif (mousePos[0] in range(217, 317) and mousePos[1] in range(237, 287)):
                    return 0
                else :
                    continue

def resetGame(window, cells, cellsIndexedStates):
    backgroundColor = (46, 59, 79)
    window.fill(backgroundColor)
    for cell in cells:
        cell.full = False
        cell.symbol = None
    for row in cellsIndexedStates:
        for col in range(3):
            row[col] = 0
    return pickBeginningState()


def main():
    windowIcon = pygame.image.load("./assets/iconProject.png")
    pygame.display.set_icon(windowIcon)

    window = pygame.display.set_mode((400, 470), pygame.NOFRAME)
    run = True
    turn = pickBeginningState()

    background = pygame.Surface((400, 470), pygame.SRCALPHA)
    background.fill((0,0,0,200))
    window.blit(background,(0,0))
    pygame.display.set_caption("TicTacToe")
    hwnd = pygame.display.get_wm_info()["window"]
    setWindowTransparency(hwnd, 100)
    setWindowRoundedCorners(hwnd, 70)

    exitRectWidth = 60
    exitRectHeight = 11
    exitRectX = 340 
    exitRectY = 2 
    exitRectWidthRange = [exitRectX, exitRectX+exitRectWidth]
    exitRectHeightRange = [exitRectY, exitRectY+exitRectHeight]

    minRectWidth = 60
    minRectHeight = 11
    minRectX = 268
    minRectY = 2 
    minRectWidthRange = [minRectX, minRectX+minRectWidth]
    minRectHeightRange = [minRectY, minRectY+minRectHeight]

    verticalWidth = 10
    verticalHeight = 400
    horizontalWidth = 400
    horizontalHeight = 10

    vertRightX = 260
    vertRightY = 15
    vertLeftX = 130
    vertLeftY = 15

    horizRightX = 0
    horizRightY = 275
    horizLeftX = 0
    horizLeftY = 145

    edgeLeftX = 0
    edgeLeftY = 15
    edgeRightX = 390
    edgeRightY = 15
    edgeTopX = 0
    edgeTopY = 15
    edgeBottomX = 0
    edgeBottomY = 405

    cell1 = Cell(10, 130, 25, 145)
    cell2 = Cell(140, 260, 25, 145)
    cell3 = Cell(270, 390, 25, 145)
    cell4 = Cell(10, 130, 155, 275)
    cell5 = Cell(140, 260, 155, 275)
    cell6 = Cell(270, 390, 155, 275)
    cell7 = Cell(10, 130, 285, 405)
    cell8 = Cell(140, 260, 285, 405)
    cell9 = Cell(270, 390, 285, 405)
    cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
    cellsIndexedStates = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    backgroundColor = (46, 59, 79)
    window.fill(backgroundColor)
    textFont = pygame.sysfont.SysFont("dutch", 26)
    while run:
        pygame.font.init()
        if run:
            gridColor = (235, 215, 255) if turn == "x" else (255, 255, 255)
            drawGrid(window, gridColor, vertRightX, vertRightY, vertLeftX, vertLeftY, horizRightX, horizRightY, horizLeftX, horizLeftY, edgeRightX, edgeRightY, edgeLeftX, edgeLeftY, edgeTopX, edgeTopY, edgeBottomX, edgeBottomY, horizontalWidth, horizontalHeight, verticalWidth, verticalHeight)
            drawExitRect(window, (240,150,190),(exitRectX,exitRectY,exitRectWidth,exitRectHeight),4)
            drawMinRect(window, (240,240,150),(minRectX,minRectY,minRectWidth,minRectHeight),4)
            turnSymbolFont = pygame.sysfont.SysFont("helvetica", 50)
            turnText = textFont.render("Current turn is :", False, gridColor)
            turnSymbol = turnSymbolFont.render(turn, False, gridColor)
            window.blit(turnText, (90, 425))
            pygame.draw.rect(window,backgroundColor,(262,424,42,42))
            window.blit(turnSymbol, (266, 408))
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = event.pos
                    conditionX = ( mousePos[0] not in range(0, 10) and mousePos[0] not in range(130, 140) and mousePos[0] not in range(260, 270) and mousePos[0] not in range(390, 400))
                    conditionY = ( mousePos[1] not in range(0, 25) and mousePos[1] not in range(145, 155) and mousePos[1] not in range(275, 285) and mousePos[1] not in range(405, 415))

                    if (mousePos[0] in range (exitRectWidthRange[0],exitRectWidthRange[1])) and (mousePos[1] in range(exitRectHeightRange[0],exitRectHeightRange[1])):
                        run = False
                        pygame.quit()
                        return

                    if (mousePos[0] in range (minRectWidthRange[0],minRectWidthRange[1])) and (mousePos[1] in range(minRectHeightRange[0],minRectHeightRange[1])):
                        minimizeWindow(hwnd)

                    if ( mousePos[0] in range(10, 390) and mousePos[1] in range(10, 390) and conditionX and conditionY):
                        selectedCell, selectedCellRow, selectedCellCol = ( getSelectedCell(mousePos, cells))
                        available = checkAvailability( selectedCell, selectedCellRow, selectedCellCol, cellsIndexedStates,)
                        if available: 
                            turn, nextTurn = markCell( selectedCell, selectedCellRow, selectedCellCol, cellsIndexedStates, turn,)
                            renderOnCell(window, selectedCell, turn, gridColor)
                            # print(f"Rendering {nextTurn} at cell({available} availability): {selectedCell.width}, {selectedCell.height}\nThe state of the grid is {cellsIndexedStates}")

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    return

        result = compareCells(cells, cellsIndexedStates)
        if result is not None:
            displayResult(window, result, backgroundColor, textFont)
            asking = True
            while asking:
                replay = askIfReplay(window, backgroundColor, textFont) 
                if not replay:
                    run = False
                    pygame.quit()
                    return
                else:
                    resetGame(window, cells, cellsIndexedStates)
                    break

    return
main()
