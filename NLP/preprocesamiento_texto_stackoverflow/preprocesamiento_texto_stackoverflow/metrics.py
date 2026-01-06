from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    auc,
    average_precision_score,
    precision_recall_curve,
    roc_curve,
)


def plot_roccurve_multilabel(y_test, y_score, n_classes, show_n=3):
    """Plots ROC curve for micro and macro averaging."""

    # Compute ROC curve and ROC area for each class
    fpr = {}
    tpr = {}
    roc_auc = {}
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    # Compute macro-average ROC curve and ROC area
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    # Plot all ROC curves
    plt.plot(
        fpr["micro"],
        tpr["micro"],
        label="micro-average ROC curve (area = {0:0.2f})".format(roc_auc["micro"]),
        color="deeppink",
        linewidth=4,
        linestyle="--",
    )

    plt.plot(
        fpr["macro"],
        tpr["macro"],
        label="macro-average ROC curve (area = {0:0.2f})".format(roc_auc["macro"]),
        color="navy",
        linewidth=4,
        linestyle="--",
    )

    colors = cycle(["aqua", "darkorange", "cornflowerblue"])
    for i, color in zip(range(0, show_n), colors):
        plt.plot(
            fpr[i],
            tpr[i],
            color=color,
            lw=2,
            linestyle=":",
            label="ROC curve of class {0} (area = {1:0.2f})".format(i, roc_auc[i]),
        )

    plt.plot([0, 1], [0, 1], "k--", lw=2)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Some extension of ROC to multi-class")
    plt.legend(loc="lower right")


def plot_prcurve_multilabel(y_test, y_score, n_classes, show_n=3):
    """Plots Precision-Recall curve for each class."""

    precision = {}
    recall = {}
    average_precision = {}
    for i in range(n_classes):
        precision[i], recall[i], _ = precision_recall_curve(y_test[:, i], y_score[:, i])
        average_precision[i] = average_precision_score(y_test[:, i], y_score[:, i])

    # macro average
    precision["macro"] = np.mean([precision[i] for i in range(n_classes)], axis=0)
    recall["macro"] = np.mean([recall[i] for i in range(n_classes)], axis=0)
    average_precision["macro"] = average_precision_score(
        y_test, y_score, average="macro"
    )

    # weighted average
    precision["weighted"] = np.sum(
        [precision[i] * np.sum(y_test[:, i]) for i in range(n_classes)], axis=0
    ) / np.sum(y_test)
    recall["weighted"] = np.sum(
        [recall[i] * np.sum(y_test[:, i]) for i in range(n_classes)], axis=0
    ) / np.sum(y_test)
    # weighet average precision
    average_precision["weighted"] = average_precision_score(
        y_test, y_score, average="weighted"
    )

    colors = cycle(["navy", "turquoise", "darkorange", "cornflowerblue", "teal"])
    for i, color in zip(range(show_n), colors):
        plt.plot(
            recall[i],
            precision[i],
            color=color,
            lw=2,
            alpha=0.7,
            linestyle=":",
            label="Precision-recall curve of class {0} (area = {1:0.2f})".format(
                i, average_precision[i]
            ),
        )

    plt.plot(
        recall["macro"],
        precision["macro"],
        color="blue",
        linestyle="--",
        alpha=0.7,
        lw=4,
        label="macro-average Precision-recall curve (area = {0:0.2f})".format(
            average_precision["macro"]
        ),
    )

    plt.plot(
        recall["weighted"],
        precision["weighted"],
        color="green",
        alpha=0.7,
        linestyle="--",
        lw=4,
        label="weighted-average Precision-recall curve (area = {0:0.2f})".format(
            average_precision["weighted"]
        ),
    )

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Extension of Precision-Recall curve to multi-class")
    plt.legend(loc="lower right")
    plt.show()
